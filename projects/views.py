from django.shortcuts import redirect, render

from .models import *


def project_list(request):
    projects = Project.objects.filter(is_active=True).order_by('-important')
    categories = Category.objects.all()

    active_category = request.GET.get('category')
    if active_category:
        projects = projects.filter(categories__id=active_category)

    return render(request, "projects.html", {
        "projects": projects,
        "categories": categories,
        "active_category": active_category,
    })


def project_detail(request, project_id):
    project = Project.objects.filter(id=project_id, is_active=True).first()
    if project is None:
        return redirect('project:projects')

    mobile_images = project.images.filter(type='mobile').order_by('number_sort')
    desktop_images = project.images.filter(type='desktop').order_by('number_sort')

    context = {
        'project': project,
        'mobile_images': mobile_images,
        'desktop_images': desktop_images
    }
    return render(request, 'project_detail.html', context)
