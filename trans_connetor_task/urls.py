"""
URL configuration for trans_connetor_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from office_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('person/', views.PersonView.as_view()),
    path('office/employees/', views.OfficeEmployeesView.as_view()),
    path('office/', views.OfficeView.as_view(), name='office'),
    path('add-employee/', views.AddEmployeeView.as_view()),
    path('update-work-history/', views.UpdateWorkHistoryView.as_view())
]
