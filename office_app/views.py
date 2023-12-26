from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from office_app.services.officeservice import OfficeService

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

