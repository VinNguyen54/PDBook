from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

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