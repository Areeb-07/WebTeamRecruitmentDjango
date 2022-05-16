from django.db import models

class Team(models.Model):
    team_name=models.CharField(max_length=255)
    team_id=models.CharField(max_length=20)
    team_member_names=models.CharField(max_length=510)
