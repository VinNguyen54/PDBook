from django.shortcuts import redirect

from apps.cart.cart import Cart

from .models import Order, OrderItem

def start_order(request):
    cart = Cart(request)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        note = request.POST.get('note')
       

        order = Order.objects.create(customer = request.user, first_name = first_name, last_name = last_name, email = email, phone = phone, address = address, note = note)

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            product.total_quantity -= quantity
            product.save()

            item = OrderItem.objects.create( order = order, product = product, price = price, quantity = quantity)

        cart.clear()
        return redirect('success')

    
    return redirect('cart')