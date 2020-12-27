from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)
        #print('Request.user:', request.user)
        #print('Request.user.id:', request.user.id)

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
        'title': 'Crear proyecto',
        'form': form
    }
    return render(request, 'nexus/home.html', context)

def success(request):
    return render(request, 'nexus/success.html')
