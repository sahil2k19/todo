from django.shortcuts import render, redirect
from .models import Todo

from .forms import TodoForm

# Create your views here.
def home(request):
    tasks = Todo.objects.all()
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form':form}
    return render(request, 'home.html', context)

def update(request, pk):
    task = Todo.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {"form":form}
    return render(request, 'update_task.html', context)


def delete(request, pk):
    task = Todo.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task': task}
    return render(request, "delete.html", context)
