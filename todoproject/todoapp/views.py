from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'todoapp/index.html')


def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'todoapp/list.html', context=mydictionary)


def delete(request, id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'todoapp/list.html', context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'todoapp/list.html', context=mydictionary)

def sortdata(request):
    mydictionary ={
        "alltodos": Todo.objects.all().order_by('-priority')
    }
    return render(request, 'todoapp/list.html', context=mydictionary)

def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos": Todo.objects.filter(title__contains=q)
    }
    return render(request, 'todoapp/list.html', context=mydictionary)

def edit(request,id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title": obj.title,
        "description": obj.description,
        "priority": obj.priority,
        "id": obj.id
    }
    return render(request, 'todoapp/edit.html', context=mydictionary)


def update(request,id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'todoapp/list.html', context=mydictionary)