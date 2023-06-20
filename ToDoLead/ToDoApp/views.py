from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import TodoListItem
from datetime import datetime
from django.http import HttpResponseRedirect

'''
class TaskListView(ListView):
    model = Tarea
    template_name = 'ToDoApp/Lista_Tareas.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'ToDoApp/Lista_Tareas.html'
    success_url = reverse_lazy('ToDoApp:Lista_Tareas')

    def form_valid(self, form):
        response = super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form, tasks=self.model.objects.all()))

class TaskUpdateView(UpdateView):
    model = Tarea
    fields = ['Titulo']
    template_name = 'ToDoApp/Actualizar_Tarea.html'
    success_url = reverse_lazy('ToDoApp:Lista_Tareas')

class TaskDeleteView(DeleteView):
    model = Tarea
    template_name = 'ToDoApp/Eliminar_Tarea.html'
    success_url = reverse_lazy('ToDoApp:Lista_Tareas')

def complete_task(request, task_id):
    task = Tarea.objects.get(id=task_id)
    if not task.completed:
        task.completed = True
        task.completed_at = datetime.now()
        task.save()
    return redirect('ToDoApp:Lista_Tareas')
'''

def todoappView(request):
    items = TodoListItem.objects.all()
    return render(request, 'ToDoApp/Lista_Tareas.html', {'all_items': items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('ToDoApp/Lista_Tareas/')

def deleteTodoItem(request):
    x = TodoListItem.objects.get(id=i)
    x.delete()
    return HttpResponseRedirect('ToDoApp/Lista_Tareas/')