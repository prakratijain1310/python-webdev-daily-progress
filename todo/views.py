from django.shortcuts import render,redirect
from todo.models import Todo

# Create your views here.
def home(request):
    tasks=Todo.objects.all()
    if request.method == 'POST':
        var1=request.POST.get('taskname')
        var2=request.POST.get('startdate')
        var3=request.POST.get('enddate')
        test_instance=Todo(taskname=var1,startdate=var2,enddate=var3)
        test_instance.save()
        return redirect("hometodo")
    return render(request,"hometodo.html",{'tasks':tasks})

def update(request,id):
    tasks=Todo.objects.get(id=id)
    if request.method == 'POST':
        var1=request.POST.get('taskname')
        var2=request.POST.get('startdate')
        var3=request.POST.get('enddate')
        tasks.taskname=var1
        tasks.startdate=var2
        tasks.enddate=var3
        tasks.save()
        return redirect("hometodo")
    return render(request,"update.html",{'tasks':tasks})
def delete(request,id):
    tasks=Todo.objects.get(id=id)
    tasks.delete()
    return redirect('hometodo')
    