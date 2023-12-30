from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todolist/add_todo.html', {'form': form})

def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def delete_completed(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('todo_list')
