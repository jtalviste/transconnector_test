from typing import List
from office_app.services.meteo import get_current_temperature
from office_app.models import Office
from office_app.models import Person
from office_app.models import WorkHistory
from django.utils import timezone

class OfficeService:
    @staticmethod
    def get_office_with_temperature(office_name) ->Office :
        # Fetch the office model by name
        office = Office.objects.get(name=office_name)

        # Use the imported method to get current temperature
        current_temperature = get_current_temperature(office.latitude, office.longitude)

        if current_temperature is not None:
            # Add the current_temperature attribute to the Office model
            office.current_temperature = current_temperature
            return office
        else:
            return None
        
    @staticmethod
    def get_office_employees(office_name:str) -> List[Person] :
        # Fetch the office model by name
        return list(Person.objects.filter(office__name=office_name) or [])
    
    @staticmethod
    def add_employee(office:Office,person:Person) :
        person.office = office
        person.save()

        workHistory = WorkHistory(office=office,person=person,last_checked=timezone.now())
        workHistory.save()
