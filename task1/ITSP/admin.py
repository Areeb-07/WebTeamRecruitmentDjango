from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display=('team_id','team_name','team_member_names')

admin.site.register(Team,TeamAdmin)
