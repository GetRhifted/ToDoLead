from django.contrib import admin
from django.urls import path
from ToDoApp import views
from ToDoApp.views import todoappView, addTodoView, deleteTodoItem

app_name = 'ToDoApp'

urlpatterns = [
    path('Lista_Tareas/', todoappView),
    path('Crear_Tarea', addTodoView),
    path('Borrar_Tarea', deleteTodoItem ),
]