import random

from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404


from .forms import CommentForm
from .models import Category, Product, Comment

from apps.cart.cart import Cart



def product(request, category_slug, product_slug):
    cart = Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)


    context = {
        'product': product,
        'similar_products': similar_products,
    }

    return render(request, 'product/product.html', context)
    
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})