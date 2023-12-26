from django.core.management.base import BaseCommand
from django.utils.timezone import now
from office_app.models import Person, WorkHistory

class Command(BaseCommand):
    help = 'Updates last_checked work history fields for all employees'

    def handle(self, *args, **options):
        for person in Person.objects.all():
            for workHistory in WorkHistory.objects.filter(person=person,office=person.office):
                workHistory.last_checked = now()
                workHistory.save()
