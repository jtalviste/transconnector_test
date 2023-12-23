from typing import List
from office_app.models import Person
from office_app.models import WorkHistory

class PersonService:

    @staticmethod
    def get_people_by_name(first_name=None,last_name=None) ->List[Person] :
        people = Person.objects
        if first_name:
            people = people.filter(first_name=first_name)
        if last_name:
            people = people.filter(last_name=last_name)
        for person in people:
            person.history = WorkHistory.objects.filter(office = person.office)
        return list(people)
