from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import login, logout

from .models import User
from .forms import CreateUserForm


def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password =  request.POST['password']

        user = User.objects.create_user(username= username,
                                         email= email, password=password) 
        login(request,user)
        return redirect('templates/login.html')
    return render(request, 'templates/register.html',status = 200)   


def loginPage(request):
    pass



