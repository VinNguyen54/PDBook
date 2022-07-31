from django.shortcuts import redirect, render

from apps.cart.cart import Cart
from .models import Order, OrderItem
# Create your views here.
def start_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        order = Order.objects.create(customer = request.user,first_name = first_name, last_name = last_name, email = email, phone = phone, address = address )

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(order = order, product = product,price = price, quantity = quantity)
        
        return redirect('success')
    return redirect('cart')
