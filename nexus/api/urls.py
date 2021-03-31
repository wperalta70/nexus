from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/<int:projectId>/team', views.project_team, name="project-team"),
    path('tickets/<int:ticketId>/assign', views.assign_ticket, name="assign-ticket")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)