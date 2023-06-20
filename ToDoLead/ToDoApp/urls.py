from django.contrib import admin
from django.urls import path
from ToDoApp import views

app_name = 'ToDoApp'

urlpatterns = [
    path('', views.ListadeTareas.as_view(), name='tarea'),
    path('tarea/<int:pk>/', views.DetalledeTarea.as_view(), name='Detalles'),
]