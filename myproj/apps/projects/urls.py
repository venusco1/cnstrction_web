from django.urls import path,include
from apps.projects import views

app_name  = 'projects'

urlpatterns = [
  path('project_details/', views.project_details, name='project_details'),
  path('project/', views.project, name='project'),
]