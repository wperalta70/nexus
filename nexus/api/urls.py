from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/<int:projectId>/team-members', views.project_team_members, name="team-members"),
    path('tickets/<int:ticketId>/assign', views.assign_ticket, name="assign-ticket")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)