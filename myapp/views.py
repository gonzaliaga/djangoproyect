from django.http import HttpResponse
from .models import Task
from .models import Project
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        title = 'Welcome to Mayami! la Ilma de Cuba'
        return render(request, 'index.html', {'title': title})
    else:
        return HttpResponse("Invalid request method")

def about(request):
    if request.method == 'GET':
        username = 'Gonzalo'
        return render(request, 'about.html', {'username': username})
    else:
        return HttpResponse("Invalid request method")

def hello(request, id):
    if request.method == 'GET':
        return HttpResponse("<h1>Hola %s ! </h1>" % id)
    else:
        return HttpResponse("Invalid request method")

def projects(request):
    if request.method == 'GET':
        #projects = list(Project.objects.values())
        projects = Project.objects.all()
        return render(request, 'projects.html', {'projects': projects})
    else:
        return HttpResponse("Invalid request method")
    
def tasks(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values())
        return render(tasks, 'tasks.html')
    else:
        return HttpResponse("Invalid request method")
