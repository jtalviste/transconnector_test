import os
from typing import List
from django.test import TestCase

from office_app.apikey import API_KEY_PROP_NAME, getAccessApiKey
from office_app.services.meteo import get_current_temperature
from office_app.services.officeservice import OfficeService
from office_app.services.personservice import PersonService
from office_app.services.workhistoryservice import WorkHistoryService
from .models import Office
from .models import Person
from .models import WorkHistory

# office fixture length check
class OfficeModelTestCase(TestCase):

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
        os.environ[API_KEY_PROP_NAME] = 'thisisahardtoguessapikey'
        self.assertEqual(getAccessApiKey(),'thisisahardtoguessapikey')

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
        officeHistory = WorkHistory.objects.filter(office=headQuarters,person=newPerson)

        self.assertEqual(len(personsInOffice),2)
        self.assertEqual(len(officeHistory),1)

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


print("TODO: # scheduled task to runs every day")
print("TODO: # scheduled task updates the last_checked field with the date on which the task is running")
print("TODO: # scheduled task can be run in batches iterated")

print("TODO: # Get office info via controller")
print("TODO: # Get office info via controller, need API key")
print("TODO: # controller test: Get employees in an office")
print("TODO: # controller test: Get employees by first name")
print("TODO: # controller test: Get employees by last name")
print("TODO: # controller test: Get employees by first name and last name")
print("TODO: # controller test: Get employees returns the office where they work and places where they have worked previously")
print("TODO: # controller test: Add new employee to an office")
print("TODO: # controller test: Update employee’s offices which they have worked at")

print("TODO: organize files")
print("TODO: dockerise")


