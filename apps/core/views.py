from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from apps.product.models import Product

from .forms import ContactForm
# Create your views here.
def home(request):
    newest_products = Product.objects.all()[0:9]

    return render(request, 'core/home.html', {'newest_products':newest_products})

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