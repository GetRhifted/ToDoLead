from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    completado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['completado']