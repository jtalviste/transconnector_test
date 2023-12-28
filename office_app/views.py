import json
from django.http import JsonResponse
from django.views import View

from office_app.services.workhistoryservice import WorkHistoryService
from .models import Office, Person
from typing import List
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from office_app.models import Person
from office_app.services.officeservice import OfficeService
from office_app.services.personservice import PersonService
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    context = {
        'message': 'This is the home page of the trans_connector_app app.'
    }
    return render(request, 'index.html', context)


class OfficeView(View):
    def get(self, request, *args, **kwargs):
        name = request.GET.get('name', None)
        if name is not None:
            result = OfficeService.get_office_with_temperature(name)
            response = model_to_dict(result);
            response["temperature"] = result.current_temperature
            return JsonResponse(response)
        else:
            return JsonResponse({"error": "Missing 'name' parameter"}, status=400)
        
class OfficeEmployeesView(View):
    def get(self, request, *args, **kwargs):
        name = request.GET.get('name', None)
        if name is not None:
            employees = OfficeService.get_office_employees(name)
            response = [model_to_dict(employee) for employee in employees]
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse({"error": "Missing 'name' parameter"}, status=400)
        
class PersonView(View):
    def get(self, request, *args, **kwargs):
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        personObjects:List[Person] = PersonService.get_people_by_name(first_name=first_name,last_name=last_name)
        response = []
        for person in personObjects:
            person_dict = model_to_dict(person)
            history_list = []
            for historyEntry in person.history.all():
                history_dict = {
                    'office': historyEntry.office.id,
                    'person': historyEntry.person.id,
                    'last_checked': historyEntry.last_checked.isoformat(),
                }
                history_list.append(history_dict)
            person_dict['history'] = history_list
            response.append(person_dict)
        return JsonResponse(response, safe=False)
    

class AddEmployeeView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        office_id = data.get('office_id', None)
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)

        if office_id is not None and first_name is not None and last_name is not None:
            office = Office.objects.get(id=office_id)
            new_person = Person(first_name=first_name, last_name=last_name)
            OfficeService.add_employee(office, new_person)

            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'error': 'Missing office_id, first_name, or last_name'}, status=400)
        
class UpdateWorkHistoryView(View):
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        person_id = data.get('person_id', None)
        office_ids = data.get('office_ids', None)

        if person_id is not None and office_ids is not None:
            try:
                person = Person.objects.get(id=person_id)
                offices = Office.objects.filter(id__in=office_ids)
                WorkHistoryService.updateWorkHistory(person, offices)
                return JsonResponse({'status': 'success'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'error', 'error': 'Person with id {} does not exist or one of the offices does not exist'.format(person_id)}, status=400)
        else:
            return JsonResponse({'status': 'error', 'error': 'Missing person_id or office_ids'}, status=400)


