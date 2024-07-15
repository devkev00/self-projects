from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList

# Create your views here.

def todolist_home(request):
    todos = TodoList.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todolist_home.html', context)

def todolist_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        todo = TodoList.objects.create(
            title=title,
            content=content,
        )
        return redirect('todolist:todolist_home')
    return render(request, 'todolist_create.html')

def todolist_delete(request, pk):
    todo = TodoList.objects.get(id=pk)
    todo.delete()
    return redirect('todolist:todolist_home')

def todolist_update(request, pk):
    todo = TodoList.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        completed = request.POST.get('completed') == 'on'

        todo.title = title
        todo.content = content
        todo.completed = completed
        todo.save()
        return redirect('todolist:todolist_home')
    return render(request, 'todolist_update.html', {'todo': todo})