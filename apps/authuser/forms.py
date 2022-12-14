from re import L
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import ModelForm
from django import forms


from .models import User
from apps.product.models import Product
from apps.orders.models import Order


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Enter Your Username...',
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Enter Your Email...',
        })
        self.fields["password1"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Enter Your Password...',
        })
        self.fields["password2"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Enter Your Password Confirmation...',
        })

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email = email, password = password)

            if not user:
                raise forms.ValidationError('User does not exits')

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')

        return super(UserLoginForm, self).clean(*args, **kwargs)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Enter Your Email...',
        })
        self.fields["password"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Enter Your Password...',
        })

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'author', 'page', 'publisher', 'publish_date', 'total_quantity', 'price', 'discount' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Category',
        })
        self.fields["image"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Image',
        })
        self.fields["title"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Title',
        })
        self.fields["description"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'textarea',
            'placeholder': 'Description',
        })
        self.fields["author"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Author',
        })
        self.fields["page"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'number',
            'placeholder': 'Page Number',
        })
        self.fields["publisher"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'text',
            'placeholder': 'Publiser',
        })
        self.fields["publish_date"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'datetime-local',
            'placeholder': 'Publish Date',
        })
        self.fields["total_quantity"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'number',
            'default': '0',
            'placeholder': 'Quantity',
        })
        self.fields["price"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'number',
            'placeholder': 'Price',
        })
        self.fields["discount"].widget.attrs.update({
            'required': '',
            'class': 'w-full mt-2 py-4 px-6 bg-white rounded-xl',
            'type': 'number',
            'default': '0',
            'placeholder': 'Discount',
        })
