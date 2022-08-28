import random
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.db.models import Q

from .forms import AddToCartForm, CommentForm
from .models import Category, Product, Comment

from apps.cart.cart import Cart

def product(request, category_slug, product_slug):
    cart =  Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        commentform = CommentForm(request.POST, instance=product)

        if form.is_valid(): 
            quantity = form.cleaned_data['quantity'] 

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

            return redirect('product', category_slug=category_slug, product_slug=product_slug)

        if commentform.is_valid():
            body = commentform.cleaned_data['body']
            created_by = commentform.cleaned_data['created_by']

            c = Comment(product = product, created_by = created_by, body = body)
            c.save() 

    else:
        form = AddToCartForm()
        commentform = CommentForm(instance=product)

    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)


    context = {
        'form':form,
        'commentForm':commentform,
        'product': product,
        'similar_products': similar_products,
    }

    return render(request, 'product/product.html', context)
    
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})