from django.shortcuts import render, redirect, get_object_or_404
from .models import todo


def index(request):
    if request.method == 'POST':
        task_name = request.POST.get('task-name')
        task_date = request.POST.get('task-date')

        todo.objects.create(
            taskname=task_name,
            taskdate=task_date
        )
        return redirect('home')

    item = todo.objects.all()
    return render(request, 'index.html', {'item': item})


def deletetask(request, id):
    task = get_object_or_404(todo, id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return redirect('home')


def updatetask(request, id):
    task = get_object_or_404(todo, id=id)

    if request.method == 'POST':
        task.taskname = request.POST.get('task-name')
        task.taskdate = request.POST.get('task-date')
        task.save()
        return redirect('home')

    return render(request, 'update.html', {'a': task})