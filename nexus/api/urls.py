from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects/(?P<projectId>\d+)/team-members', views.ProjectTeamMembersViewSet, basename="team-members")

urlpatterns = [
    path('tickets/<int:ticketId>/assign-ticket', views.assign_ticket, name="assign-ticket"),
    path('tickets/<int:ticketId>/change-priority', views.change_priority, name="change-priority"),
    path('tickets/<int:ticketId>/change-status', views.change_status, name="change-status")
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)