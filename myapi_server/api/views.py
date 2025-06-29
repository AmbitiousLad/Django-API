from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})    
