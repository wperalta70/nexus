from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# context:
#   title: Page's main title
#   breadcrumbs: Dict that contains the breadcrumb name as the key, and the href url as the value

# Create your views here.
# Index (dashboard)
def index(request):
    return redirect('projects-list')

# List of projects
def projectsList(request):
    context = {
        'title': 'Listado de proyectos',
        'breadcrumbs': { 
            'Inicio': '/',
            'Proyectos': '/projects',
            'Listado': '#'
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

def projectsDetail(request, projectId):
    project = Project.objects.get(id = projectId)
    tickets = project.tickets.all()

    context = {
        'title': 'Detalles del proyecto',
        'breadcrumbs': { 
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: '#',
        },
        'project': project,
        'tickets': tickets
    }

    return render(request, 'nexus/projectsDetail.html', context)

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
            'Crear Proyecto': '#',
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
            'Modificar Proyecto': '#',
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
            'Eliminar Proyecto': '#',
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

def ticketsDetail(request, projectId, ticketId):
    project = Project.objects.get(id = projectId)
    ticket = Ticket.objects.get(id = ticketId)

    context = {
        'title': 'Detalles del ticket',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: '/projects/' + str(projectId),
            'Ticket #' + str(ticketId): '#',
        },
        'logo_colors': [
            'primary',
            'success',
            'danger',
            'warning',
            'info'
        ],
        'project': project,
        'ticket': ticket
    }
    return render(request, 'nexus/ticketsDetail.html', context)

def ticketsCreate(request, projectId):
    project = Project.objects.get(id = projectId)

    if request.method == 'POST':
        form = CreateTicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.project = project
            ticket.user = request.user
            ticket.save()
            # TODO: Fix redirect and show message
            return redirect('projects-detail', projectId = projectId)

    form = CreateTicketForm()

    context = {
        'title': 'Crear nuevo ticket',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: '/projects/' + str(projectId),
            'Crear nuevo ticket': '#',
        },
        'projectId': projectId,
        'form': form
    }
    return render(request, 'nexus/ticketsCreate.html', context)

def ticketsDelete(request, ticketId):
    pass