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
    path('projects/<int:projectId>/tickets/<int:ticketId>', views.ticketsDetail, name = "tickets-detail"),
    path('projects/<int:projectId>/tickets/create', views.ticketsCreate, name = "tickets-create"),
    path('projects/<int:projectId>/tickets/<int:ticketId>/update', views.ticketsUpdate, name = "tickets-update"),
    path('projects/<int:projectId>/tickets/<int:ticketId>/delete', views.ticketsDelete, name = "tickets-delete"),

    # Users
    path('users/create/', views.usersCreate, name="users-create"),
    path('users/', views.usersList, name="users-list"),
    path('users/<int:userId>/update', views.usersUpdate, name="users-update"),
    
    
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)