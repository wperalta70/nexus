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
    path('users/<int:userId>/delete', views.usersDelete, name="users-delete"),
    
    
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/<int:userId>', views.profile, name="profile"),
    path('profile/<int:userId>/details', views.profileDetails, name="profile-details"),
    path('profile/<int:userId>/changePassword', views.changePassword, name="change-password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)