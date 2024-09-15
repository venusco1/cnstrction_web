from django.http import HttpResponse
from django.shortcuts import render


def project_details(request):
    return render( request, 'projects/project_details.html')

def project(request):
    return render( request, 'projects/project.html')