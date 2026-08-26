from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.project_list, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
]