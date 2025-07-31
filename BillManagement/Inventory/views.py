from django.shortcuts import render,redirect
from Inventory.models import product_details

# Create your views here.
def home_inventory(request):
    data=product_details.objects.all()
    if request.method == 'POST':
        var1=request.POST.get('productname')
        var2=request.POST.get('price')
        var3=request.POST.get('quantity')
        var4=request.POST.get('discount')
        test_instance=product_details(productname=var1,price=var2,quantity=var3,discount=var4)
        test_instance.save()
        return redirect("home_inventory")
    return render(request,"home_inventory.html",{'data':data})

def update(request,id):
    data=product_details.objects.get(id=id)
    if request.method == 'POST':
        var1=request.POST.get('productname')
        var2=request.POST.get('price')
        var3=request.POST.get('quantity')
        var4=request.POST.get('discount')
        data.productname=var1
        data.price=var2
        data.quantity=var3
        data.discount=var4
        data.save()
        return redirect("home_inventory")
    return render(request,"update_inventory.html",{'data':data})

def delete(request,id):
    data=product_details.objects.get(id=id)
    data.delete()
    return redirect('home_inventory')
