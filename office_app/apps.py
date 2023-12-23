from django.apps import AppConfig
from django.core.management import call_command

class OfficeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'office_app'


    def ready(self):
        # Load fixtures here
        call_command('migrate')
        call_command('loaddata', 'office.json')
        call_command('loaddata', 'person.json')
        call_command('loaddata', 'workhistory.json')

