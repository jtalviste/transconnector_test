from django.shortcuts import render

def index(request):
    context = {
        'message': 'This is the home page of the trans_connector_app app.'
    }
    return render(request, 'index.html', context)

