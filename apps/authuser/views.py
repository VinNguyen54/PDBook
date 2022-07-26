from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


from .forms import RegisterForm, UserLoginForm
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
def vendor_admin(request):
    vendor = request.user

    return render(request, 'authuser/vendor_admin.html', {'vendor':vendor})