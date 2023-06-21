from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tarea

from django.urls import reverse_lazy


class IniciodeSesion(LoginView):
    template_name = 'ToDoApp/Login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('ToDoApp:tarea')
        


class ListadeTareas(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'ToDoApp/Lista_Tareas.html'

class DetalledeTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'ToDoApp/Tarea.html'

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('ToDoApp:tarea')
    template_name = 'ToDoApp/Crear_Tarea.html'

class ActualizarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('ToDoApp:tarea')
    template_name = 'ToDoApp/Crear_Tarea.html'

class BorrarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tareas'
    success_url = reverse_lazy('ToDoApp:tarea')
    template_name = 'ToDoApp/Confirmacion_Borrar.html'
    
