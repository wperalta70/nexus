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
            return redirect('/projects')

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
