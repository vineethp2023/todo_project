from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .forms import TodoForm
from . models import Task
# Creates class based views here

class TaskDeleteView(DetailView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvhome')


class TaskUpdateview(UpdateView):
    model =  Task
    template_name = 'updateview.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class TaskListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
# Create your views here.
def index(request):
    return HttpResponse('Hello , Welcome to Todo app')
def add(request):
    if request.method=='POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    task = Task.objects.all()
    return render(request,'home.html',{'task':task})
def details(request):
    task = Task.objects.all()
    return render(request,'detail.html',{'task':task})
def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/add')
    return render(request,'delete.html')
def update(request,id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance = task)
    if f.is_valid():
        f.save()
        return redirect('/add')
    return render(request,'edit.html',{'f':f,'task':task})