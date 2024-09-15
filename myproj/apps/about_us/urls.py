from django.urls import path,include
from apps.about_us import views

app_name  = 'about_us'

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('contact', views.contact, name='contact'),
]