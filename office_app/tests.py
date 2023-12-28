import json
import os
from typing import List
from django.test import TestCase, Client
from office_app.apikey import API_KEY_ENV_PROP_NAME, checkAccessApiKey
from office_app.services.meteo import get_current_temperature
from office_app.services.officeservice import OfficeService
from office_app.services.personservice import PersonService
from office_app.services.workhistoryservice import WorkHistoryService
from .models import Office
from .models import Person
from .models import WorkHistory
from django.core.management import call_command
from django.utils import timezone

call_command('migrate')
call_command('loaddata', 'office.json')
call_command('loaddata', 'person.json')
call_command('loaddata', 'workhistory.json')



# office fixture length check
class OfficeModelTestCase(TestCase):
    fixtures = ["office"]

    def test_office_fixture(self):
        self.assertEqual(len(Office.objects.all()),10)

# person fixture check
class PersonModelTestCase(TestCase):

    def test_person_fixture(self):
        self.assertEqual(len(Person.objects.filter(last_name="Doe")),2)

# workhistory fixture check
class WorkHistoryModelTestCase(TestCase):

    def test_workhistory_fixture(self):
        self.assertEqual(len(WorkHistory.objects.filter(person__last_name="Lee")),2)

class ApiKeyTestCase(TestCase):

    def test_api_key_helper(self):
        # printApiKeyInstructions('apikey')
        os.environ[API_KEY_ENV_PROP_NAME] = "O6GFX73m4tIviuv8YtYcJwGy6awVSsb2QxG7iLjSfU8="
        self.assertEqual(checkAccessApiKey('apikey'),True)

class OpenMeteoTestCase(TestCase):

    def test_open_meteo_working(self):
        latitude = 37.775
        longitude = -122.4188

        temperature = get_current_temperature(latitude, longitude)

        if temperature is None:
            raise 'Failed to retrieve temperature information.'
        
class OfficeServiceGetOfficeTestCase(TestCase):

    def test_office_service_get_office(self):
        office = OfficeService.get_office_with_temperature("Headquarters")

        self.assertEqual(office.name,"Headquarters")

        if office.current_temperature is None:
            raise 'Failed to retrieve temperature information.'
        
class OfficeServiceEmployeesTestCase(TestCase):

    def test_office_employees(self):
        persons:List[Person] = OfficeService.get_office_employees("New York Office")

        self.assertEqual(len(persons),2)

    def test_office_employees_none(self):
        persons:List[Person] = OfficeService.get_office_employees("Tokyo Office")

        self.assertEqual(len(persons),0)

    def test_office_employee_add(self):
        headQuarters = Office.objects.get(id=1)
        newPerson = Person(first_name="Lily", last_name="Doe");
        
        OfficeService.add_employee(headQuarters, newPerson)
        
        personsInOffice = Person.objects.filter(office=headQuarters)
        workHistory = WorkHistory.objects.filter(office=headQuarters,person=newPerson)

        self.assertEqual(len(personsInOffice),2)
        self.assertEqual(len(workHistory),1)

class PersonByNameTestCase(TestCase):

    def test_get_johns(self):
        persons:List[Person] = PersonService.get_people_by_name(first_name="John")

        self.assertEqual(len(persons),1)

    def test_get_last_name_does(self):
        persons:List[Person] = PersonService.get_people_by_name(last_name="Doe")

        self.assertEqual(len(persons),2)

    def test_get_person_and_workplace(self):
        persons:List[Person] = PersonService.get_people_by_name(first_name="John")
        person = persons[0]

        self.assertEqual(person.office.name, "Headquarters")
        self.assertEqual(len(person.history), 1)

class WorkHistoryUpdateTestcase(TestCase):

    def update_work_history(self):
        person = Person.objects.get(id=1)
        offices = Office.objects.all()
        WorkHistoryService.updateWorkHistory(person, offices)

        history = WorkHistory.objects.filter(person=person)
        self.assertCountEqual(offices, history)

# Controller tests
os.environ[API_KEY_ENV_PROP_NAME] = "O6GFX73m4tIviuv8YtYcJwGy6awVSsb2QxG7iLjSfU8="
class GetOfficeTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_office(self):
        response = self.client.get('/office/', {'name': 'Headquarters'}, HTTP_APIKEY = 'apikey')
        self.assertEqual(response.status_code, 200)
        response_content = str(response.content, encoding='utf8')
        json_content = json.loads(response_content)
        self.assertFieldExists(json_content, "address");
        self.assertFieldExists(json_content, "city");
        self.assertFieldExists(json_content, "country");
        self.assertFieldExists(json_content, "id");
        self.assertFieldExists(json_content, "latitude");
        self.assertFieldExists(json_content, "longitude");
        self.assertFieldExists(json_content, "name");
        self.assertFieldExists(json_content, "temperature");
    
    def assertFieldExists(self, jsonObj, fieldName):
        self.assertIn(fieldName, jsonObj)
        self.assertIsNotNone(jsonObj[fieldName])
    
    
class GetOfficeEmployeesTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_office_employees(self):
        
        response = self.client.get('/office/employees/', {'name': 'Headquarters'}, HTTP_APIKEY = 'apikey')
        self.assertEqual(response.status_code, 200)
        response_content = str(response.content, encoding='utf8')
        json_content = json.loads(response_content)
        self.assertEqual(len(json_content),1)

class GetPersonTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_person(self):
        
        response = self.client.get('/person/', {'last_name': 'Doe'}, HTTP_APIKEY = 'apikey')
        self.assertEqual(response.status_code, 200)
        response_content = str(response.content, encoding='utf8')
        json_content = json.loads(response_content)
        self.assertEqual(len(json_content),2)

class GetPersonContentTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_person_content(self):
        
        response = self.client.get('/person/', {'first_name': 'John'}, HTTP_APIKEY = 'apikey')
        self.assertEqual(response.status_code, 200)
        response_content = str(response.content, encoding='utf8')
        json_content = json.loads(response_content)
        self.assertEqual(len(json_content),1)
        self.assertIsNotNone(json_content[0]["history"][0]["office"])

class AddEmployeeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_employee(self):
        response = self.client.post("/add-employee/", {
            'office_id': 1,
            'first_name': 'Joey',
            'last_name': 'Dorne'
        }, HTTP_APIKEY = 'apikey')
        self.assertEqual(response.status_code, 200)

class UpdateWorkHistoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_work_history(self):
        response = self.client.put("/update-work-history/", json.dumps({
            'person_id': 1,
            'office_ids': [1, 2]
        }), content_type='application/json', HTTP_APIKEY = 'apikey')
        self.assertEqual(response.status_code, 200)

class DateUpdateCommandTest(TestCase):

    def test_date_update_job(self):
        call_command('update_workhistory')
        workHistory = WorkHistory.objects.get(pk=1)

        # Get today's date
        today = timezone.localdate()

        # Assert that date updated
        self.assertEqual(workHistory.last_checked.date(), today)




