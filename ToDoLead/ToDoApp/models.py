from django.db import models

'''
class Tarea(models.Model):
    Titulo = models.CharField(max_length=200)
    TareaCompletada = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Titulo
'''

class TodoListItem(models.Model):
    content = models.CharField(max_length=126)