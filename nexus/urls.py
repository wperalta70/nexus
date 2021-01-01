from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    # Projects
    path('projects/', views.projectsList, name = "projects-list"),
    path('projects/<int:projectId>/', views.projectsDetail, name="projects-detail"),
    path('projects/create', views.projectsCreate, name = "projects-create"),
    path('projects/<int:projectId>/update/', views.projectsUpdate, name = "projects-update"),
    path('projects/<int:projectId>/delete/', views.projectsDelete, name = "projects-delete"),

    # Tickets
    #path('projects/<int:projectId>/tickets/<int:ticketId>', views.ticketsDetail, name = "tickets-detail"),
    path('projects/<int:projectId>/tickets/create', views.ticketsCreate, name = "tickets-create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)