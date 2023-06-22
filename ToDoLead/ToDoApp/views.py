from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Tarea

from django.urls import reverse_lazy


class IniciodeSesion(LoginView):
    template_name = 'ToDoApp/Login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('ToDoApp:tarea')
    
class RegistrodeUsuario(FormView):
    template_name = 'ToDoApp/Registro_Usuario.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('ToDoApp:tarea')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrodeUsuario, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('ToDoApp:tarea')
        return super(RegistrodeUsuario, self).get(*args, **kwargs)
   
class ListadeTareas(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'ToDoApp/Lista_Tareas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(user=self.request.user)
        context['conteo'] = context['tareas'].filter(completado=False).count()

        search_input = self.request.GET.get('barra_busqueda') or ''
        if search_input:
            context['tareas'] = context['tareas'].filter(titulo__icontains=search_input)
        
        context['search_input'] = search_input
        return context
                                 
class DetalledeTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'ToDoApp/Tarea.html'

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completado']
    success_url = reverse_lazy('ToDoApp:tarea')
    template_name = 'ToDoApp/Crear_Tarea.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearTarea, self).form_valid(form)

class ActualizarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completado']
    success_url = reverse_lazy('ToDoApp:tarea')
    template_name = 'ToDoApp/Crear_Tarea.html'

class BorrarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tareas'
    success_url = reverse_lazy('ToDoApp:tarea')
    template_name = 'ToDoApp/Confirmacion_Borrar.html'
    
