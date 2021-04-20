from django.db.models.enums import Choices
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from nexus.forms import *
from nexus.models import *
from django.contrib.auth.decorators import login_required
from nexus.decorators import *
from django.contrib.auth.models import Group

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from .serializers import *
from datetime import datetime

class ProjectTeamMembersViewSet(viewsets.ViewSet):
    # Ver el listado de miembros asignados a un proyecto
    def list(self, request, projectId):
        project = Project.objects.get(id = projectId)
        team_members = project.team_members.all()

        team_members_list = []
        for member in team_members:
            member = {
                "id": member.id,
                "name": member.get_full_name()
            }
            team_members_list.append(member)
        
        return Response(team_members_list)

    # Asignar un usuario a un proyecto
    @action(detail = False, methods=['post'])
    def assign(self, request, projectId):
        project = Project.objects.get(id = projectId)

        userId = request.data.get('userId') # Recibe {"userId": id} en el request body
        user = User.objects.get(id = userId)

        try:
            project.team_members.add(user)
            return Response(status = status.HTTP_201_CREATED)
        except Exception:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    # Remover un usuario del listado de usuarios asignados a un proyecto
    @action(detail = False, methods=['post'])
    def remove(self, request, projectId):
        project = Project.objects.get(id = projectId)

        userId = request.data.get('userId') # Recibe {"userId": id} en el request body
        user = User.objects.get(id = userId)

        try:
            project.team_members.remove(user)
            return Response(status = status.HTTP_200_OK)
        except Exception:
            return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def assign_ticket(request, ticketId):
    """
        Receives:   ´ticketId´ (url parameter), ´id´ and ´name´ (request body)
        Does:       assigns the ticket to this new user
    """

    userId = request.POST.get('userId')

    ticket = Ticket.objects.get(id = ticketId)
    user = User.objects.get(id = userId)

    ticket.assigned_to = user
    ticket.last_updated = datetime.now()
    
    try:
        ticket.save()
        return Response(status = status.HTTP_200_OK)
    except Exception:
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def change_priority(request, ticketId):
    """
        Receives:   ´ticketId´ (url parameter), ´priority´ (request body)
        Does:       changes the ticket's priority
    """

    ticket = Ticket.objects.get(id = ticketId)

    ticket.priority = request.POST.get('priority')
    ticket.last_updated = datetime.now()

    try:
        ticket.save()
        return Response(status = status.HTTP_200_OK)
    except Exception:
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def change_status(request, ticketId):
    """
        Receives:   ´ticketId´ (url parameter), ´status´ (request body)
        Does:       changes the ticket's status
    """

    ticket = Ticket.objects.get(id = ticketId)
    ticket.status = request.POST.get('status')
    ticket.last_updated = datetime.now()

    try:
        ticket.save()
        return Response(status = status.HTTP_200_OK)
    except Exception:
        return Response(status = status.HTTP_400_BAD_REQUEST)
