from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from nexus.forms import *
from nexus.models import *
from django.contrib.auth.decorators import login_required
from nexus.decorators import *
from django.contrib.auth.models import Group

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['POST'])
def assign_ticket(request, ticketId):
    ticket = Ticket.objects.get(id = ticketId)

    ticket.assigned_to = request.POST

@api_view(['GET'])
def project_team(request, projectId):
    #project = Project.objects.get(id = projectId)

    users = User.objects.all()
    users_serializer = ProjectTeamSerializer(users, many=True)

    return Response(users_serializer.data)