from django.shortcuts import render

from apps.product.models import Product
# Create your views here.
def home(request):
    newest_products = Product.objects.all()[0:9]
    
    return render(request, 'core/home.html', {'newest_products':newest_products})