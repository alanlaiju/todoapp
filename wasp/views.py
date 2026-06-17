from django.shortcuts import render,redirect
from . models import todo
def index(request):
  item=todo.objects.all()
  if request.method=='POST':
    a=request.POST.get('task-name')
    b=request.POST.get('task-date')
    todo.objects.create(taskname=a,taskdate=b)
    return redirect('home')
  return render(request, 'index.html',{'item':item})


def deletetask(request,id):
  a=todo.objects.filter(id=id)
  a.delete()
  return redirect('home')


def updatetask(request,id):
    a=todo.objects.get(id=id)
    if request.method=='POST':
     a.taskname=request.POST.get('task-name')
     a.taskdate=request.POST.get('task-date')
     a.save()
     return redirect('home')
    return render(request, 'update.html', {'a':a})

# Create your views here.
