from rest_framework import serializers
from nexus.models import *

class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']