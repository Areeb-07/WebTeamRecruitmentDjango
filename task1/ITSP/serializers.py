from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('team_id', 'team_name', 'team_member_names')