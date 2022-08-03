from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


from .forms import RegisterForm, UserLoginForm, ProductForm
from apps.product.models import Product
from apps.orders.models import Order
# Create your views here.

def register(request):
    if request.method == 'POST':
        form =RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')

    else:
        form =RegisterForm()

    return render(request, 'authuser/register.html', {'form':form})


def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(email = email, password = password)

            login(request, user)

            if user.is_staff :
                return redirect('vendor_admin')
            else:
                return redirect('home')
    else:

        form =UserLoginForm()

    return render(request, 'authuser/login.html', {'form':form})

@login_required
def customer_admin(request):
    customer = request.user
    orders = customer.orders.all()

    return render(request, 'authuser/customer_admin.html', {'customer':customer, 'orders':orders})

@login_required
def vendor_admin(request):
    vendor = request.user
    products = vendor.products.all()
    orders = Order.objects.all()

    return render(request, 'authuser/vendor_admin.html', {'vendor':vendor, 'products':products, 'orders':orders})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'authuser/add_product.html', {'form': form})

@login_required
def edit_product(request, pk):
    vendor = request.user
    product = vendor.products.get(pk = pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return redirect('vendor_admin')

    else:
        form = ProductForm(instance=product) 

    return render(request, 'authuser/edit_product.html', {'form':form, 'product':product})
