from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

from .forms import RegistrationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate username and password fields
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('myapp:index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please enter a username and password.')
    return render(request, 'myapp/authentication/login.html')

def index(request):
    # Your logic to render the index page
    return render(request, 'myapp/index.html')

def home_view(request):
    return render(request, 'myapp/home.html')

def about_view(request):
    return render(request, 'myapp/about.html')

def contact_view(request):
    return render(request, 'myapp/contact.html')
def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password == confirm_password:
            # Create a new user using the default Django user model
            user = User.objects.create_user(username=username, password=password)
            # You can perform additional operations on the user if needed

            # Redirect to a success page or perform any other desired action
            return render(request, 'myapp/authentication/success.html')
        else:
            # Handle password mismatch error
            return render(request, 'myapp/authentication/error.html')
    else:
        # Render the registration form
        return render(request, 'myapp/authentication/register.html')
