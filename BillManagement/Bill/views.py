from django.shortcuts import render, redirect
from Bill.models import Bill, Customer

def home_bill(request):
    if request.method == 'POST':
        name = request.POST.get('customername')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')

        product_names = request.POST.getlist('productname[]')
        prices = request.POST.getlist('price[]')
        quantities = request.POST.getlist('quantity[]')
        discounts = request.POST.getlist('discount[]')

        customer = Customer.objects.create(name=name, mobile=mobile, email=email, address=address)

        for i in range(len(product_names)):
            Bill.objects.create(
                customer=customer,
                productname=product_names[i],
                price=prices[i],
                quantity=quantities[i],
                discount=discounts[i]
            )

        return redirect('home_bill')

    return render(request, 'home_bill.html', {
        'data1': Customer.objects.last(), 
        'data2': Bill.objects.filter(customer=Customer.objects.last()) if Customer.objects.exists() else []
    })
