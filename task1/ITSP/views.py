from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from rest_framework import viewsets
from .serializers import TeamSerializer

def index(request):
    teams=Team.objects.all()
    return render(request, 'index.html', {'teams':teams})

def next1(request):
    return render(request,'next1.html')

def next2(request):
    return render(request,'next2.html')

def next3(request):
    return render(request,'next3.html')

def next4(request):
    return render(request,'next4.html')

def next5(request):
    return render(request,'next5.html')

def next6(request):
    return render(request,'next6.html')

def next7(request):
    return render(request,'next7.html')

def next8(request):
    return render(request,'next8.html')

def next9(request):
    return render(request,'next9.html')

def next10(request):
    return render(request,'next10.html')

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('team_id')
    serializer_class = TeamSerializer