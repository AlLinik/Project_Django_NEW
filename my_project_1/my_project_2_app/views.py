from django.shortcuts import render
from .models import Task


def index(request):
    task = Task.objects.all()
    return render(request, 'app/index.html', {'title': 'Главная страница', 'tasks': 'title'})


def about(request):
    return render(request, 'app/about.html')

