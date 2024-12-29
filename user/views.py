from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages  # Import messages
from django.contrib.auth import authenticate,logout
# Create your views here.
def home(request):
    return render(request,'home.html')

def register_view(request):
    if request.method == "POST":
        # Use `get` to retrieve data from request.POST safely
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Validate the passwords
        if password == confirm_password:
            try:
                # Create the user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                # Log the user in
                login(request, user)
                # Redirect to the home view
                return redirect('home')
            except Exception as e:
                # Handle exceptions such as duplicate usernames
                messages.error(request, f'Error: {e}')
        else:
            messages.error(request, "Passwords do not match")
    
    # Render the registration form
    return render(request, "register/register.html")


def login_view(request):
    if request.method == "POST":
        username =  request.POST('username')
        password = request.POST('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid password")
            
    return render(request,"register/login.html") 


def logout_view(request):
    logout(request)
    return redirect('login')