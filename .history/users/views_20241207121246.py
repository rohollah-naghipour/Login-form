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
        return redirect('login.html')
    return render(request, 'register.html',status = 200)   


def loginPage(request):
    print("after methodddddddd")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            print("after loginnnnnnnnnnnnnnnnnnnnnnn")
            return redirect('Home.html')
        else:
            return render(request, 'login.html', status=200)
        
    #return redirect('accounts:sucess_view')

