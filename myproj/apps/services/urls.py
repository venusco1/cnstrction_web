from django.urls import path,include
from apps.services import views

app_name  = 'services'

urlpatterns = [
  
    path('services_details/', views.services_details, name='services_details'),
    path('services/', views.services, name='services'),
]