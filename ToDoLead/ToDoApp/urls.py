from django.contrib import admin
from django.urls import path
from ToDoApp import views
from django.contrib.auth.views import LogoutView

app_name = 'ToDoApp'

urlpatterns = [
    path('login/', views.IniciodeSesion.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='ToDoApp:login'), name='logout'),
    path('registro_usuario/', views.RegistrodeUsuario.as_view(), name='registro_usuario'),

    path('', views.ListadeTareas.as_view(), name='tarea'),
    path('tarea/<int:pk>/', views.DetalledeTarea.as_view(), name='Detalles'),
    path('crear_tarea/', views.CrearTarea.as_view(), name='crear_tarea'),
    path('actualizar_tarea/<int:pk>/', views.ActualizarTarea.as_view(), name='actualizar_tarea'),
    path('borrar_tarea/<int:pk>/', views.BorrarTarea.as_view(), name='borrar_tarea'),
]