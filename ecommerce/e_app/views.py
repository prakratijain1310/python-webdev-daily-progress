from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.db.models import Sum, F ,Count
from django.http import JsonResponse
import qrcode
import base64
from io import BytesIO
from .models import Product, Cart
from django.contrib.auth.decorators import login_required
import random


def home(request):
    return render(request, 'home.html')  # Just show the 2 buttons


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        else:
            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Auto-login after signup
            auth_login(request, user)
            messages.success(request, "Signup successful! Welcome!")
            return redirect('main')  # Redirect to main page

    return render(request, 'signup.html')


# LOGIN
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('main')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')


def main(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    return render(request, 'main.html', {'username': request.user.username})



@login_required
def seller(request):
    # Add product
    if request.method == "POST" and 'add_product' in request.POST:
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        Product.objects.create(
            seller=request.user,
            name=name,
            description=description,
            price=price,
            image=image,
            category=category
        )
        messages.success(request, "Product added successfully!")

    # Update product
    if request.method == "POST" and 'update_product' in request.POST:
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        product = get_object_or_404(Product, id=product_id, seller=request.user)
        product.name = name
        product.description = description
        product.price = price
        product.category = category
        if image:
            product.image = image
        product.save()
        messages.success(request, "Product updated successfully!")

    # Delete product
    if request.method == "POST" and 'delete_product' in request.POST:
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id, seller=request.user)
        product.delete()
        messages.success(request, "Product deleted successfully!")

    # Show seller products
    seller_products = Product.objects.filter(seller=request.user)

    return render(request, 'seller.html', {
        'username': request.user.username,
        'products': seller_products
    })


# ------------------- Customer -------------------
@login_required

def customer(request):
    selected_category = request.GET.get('category', '')

    # Filter products by category or show random 8 if no category selected
    if selected_category:
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all().order_by('?')[:8]

    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()

    # Handle Add to Cart
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, f"{product.name} added to cart!")
        return redirect('customer')  # Refresh page after adding

    return render(request, 'customer.html', {
        'username': request.user.username,
        'products': products,
        'cart_count': cart_count,
        'selected_category': selected_category
    })
# ------------------- Cart -------------------
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    total_amount = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0

    if request.method == "POST":
        payment_method = request.POST.get('payment_method')

        if payment_method == "COD":
            # Clear the cart and confirm order
            cart_items.delete()
            messages.success(request, "Order placed successfully with Cash on Delivery!")
            return redirect('customer')

        elif payment_method == "UPI":
            # Generate QR Code for payment
            upi_string = f"upi://pay?pa=merchant@upi&pn=EcommerceStore&am={total_amount}&cu=INR"
            qr = qrcode.make(upi_string)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode()

            return render(request, 'checkout.html', {
                'username': request.user.username,
                'cart_items': cart_items,
                'total_amount': total_amount,
                'qr_code': qr_base64,  # Pass QR to template
                'show_payment_options': True
            })

    return render(request, 'checkout.html', {
        'username': request.user.username,
        'cart_items': cart_items,
        'total_amount': total_amount,
        'show_payment_options': True
    })

