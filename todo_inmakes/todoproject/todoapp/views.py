from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import taskforms
from . models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Tlistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task1'

class Tdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task2'


class Tupdateview(UpdateView):
    model = task
    template_name = 'edit.html'
    context_object_name = 'task3'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy("detailview",kwargs={'pk':self.object.id})

class Tdeleteview(DetailView):
    model = task
    template_name = 'delete.html'
    success_url=reverse_lazy('listview')




def add(request):
    taskdata=task.objects.all()
    if request.method=="POST":
        name=request.POST.get('name','')
        prior=request.POST.get('priority','')
        date=request.POST.get('date','')
        Taskdb=task(name=name,priority=prior,date=date)
        Taskdb.save()

    return render(request,"home.html",{'task1':taskdata})

def delete(request,taskid):
    taskdelete=task.objects.get(id=taskid)
    if request.method=="POST":
        taskdelete.delete()
        return redirect("/")
    return render(request,"delete.html")

def update(request,id):
    obj2=task.objects.get(id=id)
    obj3=taskforms(request.POST or None, request.FILES,instance=obj2)
    if obj3.is_valid():
        obj3.save()
        return redirect('/')

    return render(request,"update.html",{'forms':obj3,'task':obj2})

