from django.http import HttpResponse
from .models import Task
from .models import Project
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        title = 'Welcome to Mayami! mi güey'
        return render(request, 'index.html', {'title': title})
    else:
        return HttpResponse("Invalid request method")

def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')
    else:
        return HttpResponse("Invalid request method")

def hello(request, id):
    if request.method == 'GET':
        return HttpResponse("<h1>Hola %s ! </h1>" % id)
    else:
        return HttpResponse("Invalid request method")

def projects(request):
    if request.method == 'GET':
        projects = list(Project.objects.values())
        return render(projects, 'projects.html')
    else:
        return HttpResponse("Invalid request method")
    
def tasks(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values())
        return render(tasks, 'tasks.html')
    else:
        return HttpResponse("Invalid request method")
