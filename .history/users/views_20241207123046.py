from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout 

from .models import User
from .forms import CreateUserForm


def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username= username, email= email, password=password) 
        login(request,user)
        return redirect('login/')
    return render(request, 'register.html',status = 200)   


def loginPage(request):
    if request.method == 'POST':
        # Extracting the username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticating user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page or any other page after login
        else:
            # Return the same login page with an error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    # For GET request, render the login page
    return render(request, 'login.html')























#def loginPage(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(request, username = username, password=password)
        #if user is not None:
            #login(request, user)
            #return render(request, 'Home.html', {'sucsess': 'valid user'})
            #return redirect('Home.html')
        #else:
            #return render(request, 'login.html', status=200)
        
    #return redirect('accounts:sucess_view')

