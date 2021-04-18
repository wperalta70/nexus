from django.db.models.enums import Choices
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from nexus.forms import *
from nexus.models import *
from django.contrib.auth.decorators import login_required
from nexus.decorators import *
from django.contrib.auth.models import Group

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from datetime import datetime

@api_view(['GET', 'POST'])
def project_team_members(request, projectId):
    """
        GET:
            Receives:   projectId(url parameter)
            Does:       returns a list of the project's team members
        POST:
            Receives:   projectId(url parameter), userId(request body)
            Does:       adds a user as a new team member
    """
    
    project = Project.objects.get(id = projectId)

    if request.method == 'GET':
        team_members = project.team_members.all()

        team_members_list = []
        for member in team_members:
            member = {
                "id": member.id,
                "name": member.get_full_name()
            }
            team_members_list.append(member)
        
        return Response(team_members_list)
    
    elif request.method == 'POST':

        userId = request.POST.get('userId')
        user = User.objects.get(id = userId)

        try:
            project.team_members.add(user)
            return Response(status = status.HTTP_201_CREATED)
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
