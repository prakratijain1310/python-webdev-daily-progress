from django.shortcuts import render,  HttpResponse , redirect
from test_app.models import test

def home(request):
    return render(request,"home.html")

def contact_us(request):
    if request.method == 'POST':
        var1=request.POST.get('name')
        var2=request.POST.get('number')
        test_instance=test(name=var1,number=var2)
        test_instance.save()
        return redirect("home")
    return render(request,"contact_us.html")

def about_us(request):
    return render(request,"about_us.html")
