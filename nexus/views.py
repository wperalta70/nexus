from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import datetime

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

# Project details
def projectsDetail(request, projectId):
    project = Project.objects.get(id = projectId)
    tickets = project.tickets.exclude(status = "CERRADO")

    context = {
        'title': 'Detalles del proyecto',
        'breadcrumbs': { 
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: '#',
        },
        'ticketsNuevos': project.tickets.filter(status = "NUEVO").count(),
        'ticketsAsignados': project.tickets.filter(status = "ASIGNADO").count(),
        'ticketsEnProgreso': project.tickets.filter(status = "EN PROGRESO").count(),
        'ticketsCerrados': project.tickets.filter(status = "CERRADO").count(),
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
            project = form.save(commit = False)
            project.last_updated = datetime.datetime.now()
            project.save()

        return redirect('projects-detail', projectId = projectId)

    context = {
        'title': 'Modificar Proyecto',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            'Modificar Proyecto': '#',
        },
        'projectId': projectId,
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

# Ticket details
def ticketsDetail(request, projectId, ticketId):
    project = Project.objects.get(id = projectId)
    ticket = Ticket.objects.get(id = ticketId)
    comments = Comment.objects.filter(ticket = ticketId).order_by('-id')

    if request.method == 'POST':

        # Add comment
        if 'addCommentBtn' in request.POST:
            commentForm = CreateCommentForm(request.POST)

            if commentForm.is_valid:
                comment = commentForm.save(commit = False)
                comment.user = request.user
                comment.ticket = ticket
                comment.save()

        # Delete comment
        if 'deleteCommentModalBtn' in request.POST:
            commentId = request.POST.get("commentIdModal")

            comment = Comment.objects.get(id = commentId)
            comment.delete()

        return redirect('tickets-detail', projectId = projectId, ticketId = ticketId)

    commentForm = CreateCommentForm()

    context = {
        'title': 'Detalles del ticket',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: f'/projects/{projectId}',
            f'Ticket #{ticketId}': '#',
        },
        'logo_colors': [
            'primary',
            'success',
            'danger',
            'warning',
            'info'
        ],
        'project': project,
        'ticket': ticket,
        'commentForm': commentForm,
        'comments': comments
    }
    return render(request, 'nexus/ticketsDetail.html', context)

# Create ticket
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
            project.title: f'/projects/{projectId}',
            'Crear nuevo ticket': '#',
        },
        'projectId': projectId,
        'form': form
    }
    return render(request, 'nexus/ticketsCreate.html', context)

# Update ticket
def ticketsUpdate(request, projectId, ticketId):
    project = Project.objects.get(id = projectId)
    ticket = Ticket.objects.get(id = ticketId)

    form = UpdateTicketForm(instance = ticket)

    if request.method == 'POST':
        form = UpdateTicketForm(request.POST, instance = ticket)

        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.last_updated = datetime.datetime.now()
            ticket.save()

        return redirect('tickets-detail', projectId = projectId, ticketId = ticketId)

    context = {
        'title': 'Modificar Ticket',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: f'/projects/{projectId}',
            f'Ticket #{ticketId}': f'/projects/{projectId}/tickets/{ticketId}',
            'Modificar Ticket': '#',
        },
        'projectId': projectId,
        'form': form
    }

    return render(request, 'nexus/ticketsUpdate.html', context)

# Delete ticket
def ticketsDelete(request, projectId, ticketId):
    project = Project.objects.get(id = projectId)
    ticket = Ticket.objects.get(id = ticketId)

    if request.method == 'POST':
        ticket.delete()
        return redirect('projects-detail', projectId = projectId)

    context = {
        'title': 'Eliminar Ticket',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: f'/projects/{projectId}',
            f'Ticket #{ticketId}': f'/projects/{projectId}/tickets/{ticketId}',
            'Eliminar Ticket': '#',
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
    return render(request, 'nexus/ticketsDelete.html', context)