from django.shortcuts import render, get_object_or_404
from .models import *

def project_list(request):
    projects = Project.objects.filter(is_active=True).order_by('-important')

    return render(request, "projects.html", {
        "projects": projects
    })

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, is_active=True)
    mobile_images = project.images.filter(type='mobile')
    desktop_images = project.images.filter(type='desktop')
    
    context = {
        'project': project,
        'mobile_images': mobile_images,
        'desktop_images': desktop_images
    }
    return render(request, 'project_detail.html', context)