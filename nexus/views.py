from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# context:
#   title: Page's main title
#   breadcrumbs: Dict that contains the breadcrumb name as the key, and the href url as the value

# Create your views here.

# List of projects
def projectsList(request):
    context = {
        'title': 'Listado de proyectos',
        'breadcrumbs': { 
            'Inicio': '/',
            'Proyectos': '/projects',
            'Listado': '/projects'
        },
        'projects': Project.objects.all(),
        'logo_colors': [
            'primary',
            'success',
            'danger',
            'warning',
            'info'
        ]
    }

    return render(request, 'nexus/projectsList.html', context)

# Create project
def projectsCreate(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)

        if form.is_valid():
            # save(commit = False) returns a model object that hasn't been saved to the database yet
            # allowing me to do extra processing on the object before saving it
            # in this case, I do it to fill the user field with the request's user, and then I save it
            project = form.save(commit = False)
            project.user = request.user
            project.save()
            # TODO: Fix redirect and show message
            return redirect('projects-list')

    form = CreateProjectForm()

    context = {
        'title': 'Crear Proyecto',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            'Crear Proyecto': '/projects/create',
        },
        'form': form
    }

    return render(request, 'nexus/projectsCreate.html', context)

# Update project
def projectsUpdate(request, projectId):
    project = Project.objects.get(id = projectId)

    form = UpdateProjectForm(instance = project)

    if request.method == 'POST':
        form = UpdateProjectForm(request.POST, request.FILES, instance = project)

        if form.is_valid():
            form.save()

        return redirect('projects-list')

    context = {
        'title': 'Modificar Proyecto',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            'Modificar Proyecto': '{% url "projects-update" projectId %}',
        },
        'form': form
    }

    return render(request, 'nexus/projectsUpdate.html', context)

# Delete project
def projectsDelete(request, projectId):
    project = Project.objects.get(id = projectId)

    if request.method == 'POST':
        project.delete()
        return redirect('projects-list')

    context = {
        'title': 'Eliminar Proyecto',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            'Crear Proyecto': '/projects/create',
        },
        'logo_colors': [
            'primary',
            'success',
            'danger',
            'warning',
            'info'
        ],
        'project': project
    }
    return render(request, 'nexus/projectsDelete.html', context)
