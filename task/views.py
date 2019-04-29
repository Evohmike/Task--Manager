from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Task

# Create your views here.


def home(request):
    return HttpResponse("Welcome to simple project Dashboard")


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
