from django.http import HttpResponse
from django.shortcuts import render

def services_details(request):
    return render( request, 'services/services_details.html')

def services(request):
    return render( request, 'services/services.html')