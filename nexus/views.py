from django.shortcuts import render, redirect
from .forms import *
from .models import *
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group

# context:
#   title: Page's main title
#   breadcrumbs: Dict that contains the breadcrumb name as the key, and the href url as the value

# Create your views here.
# Index (dashboard)
@login_required(login_url='login')
def index(request):
    # TODO: Add context with 'tab' and 'section' variables
    return redirect('projects-list')

# List of projects
@login_required(login_url='login')
def projectsList(request):
    context = {
        'title': 'Listado de proyectos',
        'breadcrumbs': { 
            'Inicio': '/',
            'Proyectos': '/projects',
            'Listado': '#'
        },
        'tab': 'proyectos',
        'section': 'proyectos',
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
@login_required(login_url='login')
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
        'tab': 'proyectos',
        'section': 'proyectos',
        'ticketsNuevos': project.tickets.filter(status = "NUEVO").count(),
        'ticketsAsignados': project.tickets.filter(status = "ASIGNADO").count(),
        'ticketsEnDesarrollo': project.tickets.filter(status = "EN DESARROLLO").count(),
        'ticketsCerrados': project.tickets.filter(status = "CERRADO").count(),
        'project': project,
        'tickets': tickets
    }

    return render(request, 'nexus/projectsDetail.html', context)

# Create project
@login_required(login_url='login')
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
        'tab': 'proyectos',
        'section': 'proyectos',
        'form': form
    }

    return render(request, 'nexus/projectsCreate.html', context)

# Update project
@login_required(login_url='login')
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
        'tab': 'proyectos',
        'section': 'proyectos',
        'projectId': projectId,
        'form': form
    }

    return render(request, 'nexus/projectsUpdate.html', context)

# Delete project
@login_required(login_url='login')
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
        'tab': 'proyectos',
        'section': 'proyectos',
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
@login_required(login_url='login')
def ticketsDetail(request, projectId, ticketId):
    project = Project.objects.get(id = projectId)
    ticket = Ticket.objects.get(id = ticketId)
    comments = Comment.objects.filter(ticket = ticketId).order_by('-id')
    files = TicketFile.objects.filter(ticket = ticketId)

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
            commentId = request.POST.get("commentId")

            comment = Comment.objects.get(id = commentId)
            comment.delete()

        # File upload
        if 'uploadFileBtn' in request.POST:
            uploadFileForm = TicketFileUploadForm(request.POST, request.FILES)

            if uploadFileForm.is_valid:
                file = uploadFileForm.save(commit = False)
                file.user = request.user
                file.ticket = ticket
                file.save()

        # File delete
        if 'deleteFileModalBtn' in request.POST:
            fileId = request.POST.get("fileId")

            file = TicketFile.objects.get(id = fileId)
            file.delete()

        return redirect('tickets-detail', projectId = projectId, ticketId = ticketId)

    commentForm = CreateCommentForm()
    fileUploadForm = TicketFileUploadForm()

    context = {
        'title': 'Detalles del ticket',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: f'/projects/{projectId}',
            f'Ticket #{ticketId}': '#',
        },
        'tab': 'proyectos',
        'section': 'tickets',
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
        'comments': comments,
        'fileUploadForm': fileUploadForm,
        'files': files
    }
    return render(request, 'nexus/ticketsDetail.html', context)

# Create ticket
@login_required(login_url='login')
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
        'tab': 'proyectos',
        'section': 'tickets',
        'projectId': projectId,
        'form': form
    }
    return render(request, 'nexus/ticketsCreate.html', context)

# Update ticket
@login_required(login_url='login')
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
        'tab': 'proyectos',
        'section': 'tickets',
        'ticket': ticket,
        'form': form
    }

    return render(request, 'nexus/ticketsUpdate.html', context)

# Delete ticket
@login_required(login_url='login')
def ticketsDelete(request, projectId, ticketId):
    project = Project.objects.get(id = projectId)
    ticket = Ticket.objects.get(id = ticketId)

    context = {
        'title': 'Eliminar Ticket',
        'breadcrumbs': {
            'Inicio': '/',
            'Proyectos': '/projects',
            project.title: f'/projects/{projectId}',
            f'Ticket #{ticketId}': f'/projects/{projectId}/tickets/{ticketId}',
            'Eliminar Ticket': '#',
        },
        'tab': 'proyectos',
        'section': 'tickets',
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

# User login
@check_login
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectos.')

    return render(request, 'nexus/login.html')

# User logout
def userLogout(request):
    logout(request)

    return redirect('login')

# Users list
@login_required(login_url='login')
# TODO: Also allow project managers?
@allowed_users(allowed_roles=['admin'])
def usersList(request):
    users = User.objects.filter(is_active = True).all()

    if request.method == 'POST':
        pass

    context = {
        'title': 'Listado de Usuarios',
        'breadcrumbs': {
            'Inicio': '/',
            'Usuarios': '#',
        },
        'tab': 'usuarios',
        'section': 'gestionar_usuarios',
        'logo_colors': [
            'primary',
            'success',
            'danger',
            'warning',
            'info'
        ],
        'users': users,
    }
    return render(request, 'nexus/usersList.html', context)


# Create user
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def usersCreate(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            role = request.POST.get("role")
            group = Group.objects.get(name = role)
            user.groups.add(group)

            # TODO: Change to redirect('users-list')
            return redirect('projects-list')

    context = {
        'title': 'Crear Usuario',
        'breadcrumbs': {
            'Inicio': '/',
            'Usuarios': '/users',
            'Crear Usuario': '#',
        },
        'tab': 'usuarios',
        'section': 'crear_usuario',
        'form': form
    }

    return render(request, 'nexus/usersCreate.html', context)

# Update user
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'project_manager', 'developer', 'tester'])
def usersUpdate(request, userId):
    user = User.objects.get(id = userId)

    user_form = UpdateUserForm(instance = user)
    profile_form = UpdateProfileForm(instance = user.profile)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance = user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance = user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Se han actualizado los datos de su perfil.')
            # TODO: Change redirect based on if the user changed his profile, or if an admin changed another user's profile
            return redirect('users-list')

    context = {
        'title': 'Modificar Usuario',
        'breadcrumbs': {
            'Inicio': '/',
            'Usuarios': '/users',
            request.user.get_full_name(): f'/users/{request.user.id}',
            'Modificar Usuario': '#',
        },
        'tab': 'usuarios',
        'section': 'gestionar_usuarios',
        'user': user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'nexus/usersUpdate.html', context)

# Delete user
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def usersDelete(request, userId):
    user = User.objects.get(id = userId)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        messages.success(request, 'El usuario se ha dado de baja.')
        return redirect('users-list')

    context = {
        'title': 'Modificar Usuario',
        'breadcrumbs': {
            'Inicio': '/',
            'Usuarios': '/users',
            request.user.get_full_name(): f'/users/{request.user.id}',
            'Eliminar Usuario': '#',
        },
        'tab': 'usuarios',
        'section': 'gestionar_usuarios',
        'user': user
    }
    return render(request, 'nexus/usersDelete.html', context)


@login_required(login_url='login')
def profile(request, userId):
    user = User.objects.get(id = userId)

    context = {
        'title': f'Perfil de {user.get_full_name()}',
        'breadcrumbs': {
            'Inicio': '/',
            'Mi perfil': '#',
        },
        'tab': 'usuarios',
        #'section': 'gestionar_usuarios',
        'user': user
    }
    return render(request, 'nexus/profile.html', context)