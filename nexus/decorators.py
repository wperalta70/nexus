from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def check_login(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view(request, *args, **kwargs)

    return wrapper

def allowed_users(allowed_roles = []):
    def decorator(view):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view(request, *args, **kwargs)
            else:
                messages.warning(request, 'Este usuario no tiene los permisos necesarios para ver esa página.')
                return redirect('index')
        return wrapper
    return decorator