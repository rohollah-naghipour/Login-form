from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login,authenticate

from .models import User




# my_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # For displaying messages
from .form import UserRegistrationForm, UserLoginForm # Import your forms

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') # Redirect authenticated users from registration

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login') # Redirect to login page after successful registration
        else:
            # If form is not valid, errors will be in form.errors
            pass # The form will be re-rendered with errors below
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home') # Redirect authenticated users from login

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Welcome, {username}!')
                return redirect('home') # Redirect to your home page
            else:
                messages.error(request, 'Invalid username or password.')
        # If form is not valid, errors will be in form.errors
        # and the form will be re-rendered below
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)

# Example home page view (you'll need to define this)
def homePage(request):
    return render(request, 'home.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login') # Redirect to login page after logout









#def registerPage(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #email = request.POST['email']
        #password = request.POST['password']
        #user = User.objects.create_user(username = username, email= email, password = password) 
        #login(request,user)
        #return redirect('login/')
    #return render(request, 'register.html',status = 200)   


#def loginPage(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']

        #user = authenticate(request, username = username, password = password)
        #if user is not None:
            #login(request, user)
            #return redirect('Home/')
        #else:
            #return render(request, 'login.html', {'error': 'Invalid username or password'})
    #return render(request, 'login.html')      



#def homepage(request):
    #return render(request, 'Home.html', status=200)

