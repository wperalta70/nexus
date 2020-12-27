from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def projectsList(request):
    context = {
        'title': 'Listado de proyectos',
        'projects': Project.objects.all()
    }

    return render(request, 'nexus/projectsList.html', context)

def projectsCreate(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)

        if form.is_valid():
            # save(commit = False) returns a model object that hasn't been saved to the database yet
            # allowing me to do extra processing on the object before saving it
            # in this case, I do it to fill the user field with the request's user
            # and then I save it
            project = form.save(commit = False)
            project.user = request.user
            project.save()
            return redirect('/success/')

    form = CreateProjectForm()

    context = {
        'title': 'Crear Proyecto',
        'form': form
    }
    return render(request, 'nexus/projectsCreate.html', context)
