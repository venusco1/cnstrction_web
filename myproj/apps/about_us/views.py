from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render( request, 'index.html')

def about(request):
    return render( request, 'about_us/about.html')

def contact(request):
    return render( request, 'about_us/contact.html')