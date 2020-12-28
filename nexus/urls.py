from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/', views.projectsList, name = "projects-list"),
    path('projects/create', views.projectsCreate, name = "projects-create"),
    path('projects/<int:projectId>/update/', views.projectsUpdate, name = "projects-update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)