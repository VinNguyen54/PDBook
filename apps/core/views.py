from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from django.db.models import Q

from apps.product.models import Product, Category

from .forms import ContactForm
# Create your views here.
def home(request):
    newest_products = Product.objects.all()[0:10]

    return render(request, 'core/home.html', {'newest_products':newest_products})

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category =request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    
    if query:
        products = products.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context= {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'core/shop.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('core/emails/contactform.html', {
                'name':name,
                'email': email,
                'content': content
            })

            print('the form is valid')

            send_mail('The contact form subject', 'this is the message', 'noreply@PDshop.com', ['PDshop542@gmail.com'], html_message=html)

        return redirect('contact')
    else: 
        form  = ContactForm()
    return render(request, 'core/contact.html', {'form':form})