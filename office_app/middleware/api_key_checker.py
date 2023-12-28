from django.http import JsonResponse

from office_app.apikey import checkAccessApiKey

class ApiKeyCheckerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('Apikey')
        if not checkAccessApiKey(api_key):
            return JsonResponse({'error': 'Invalid API_KEY in headers'}, status=500)

        response = self.get_response(request)

        return response
