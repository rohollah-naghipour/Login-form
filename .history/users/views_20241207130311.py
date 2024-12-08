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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')      


#def loginPage(request):
    #if request.method == 'POST':
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        
        #user = authenticate(request, username=username, password=password)
        
        #if user is not None:
            #print("sknfkndjbfd")
            #login(request, user)
            #return redirect('Home/')  
        #else:
            #return render(request, 'login.html', {'error': 'Invalid username or password'})
    #return render(request, 'login.html')


def homepage(request):
    return render(request, 'Home.html', status=200)
