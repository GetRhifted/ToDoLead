from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tarea

class ListadeTareas(ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'ToDoApp/Lista_Tareas.html'

class DetalledeTarea(DetailView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'ToDoApp/Tarea.html'