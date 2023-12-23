from typing import List
from office_app.models import Office
from office_app.models import Person
from office_app.models import WorkHistory
from django.utils import timezone

class WorkHistoryService:

    @staticmethod
    def updateWorkHistory(person:Person,history:List[Office]) ->List[Person] :
        WorkHistory.objects.filter(person=person).delete()
        for office in history:
            newHistoryEntry = WorkHistory(person=person,office=office,last_checked=timezone.now())
            newHistoryEntry.save();
