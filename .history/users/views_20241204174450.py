from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()

    if request == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("user created OK 200 ")
        if not form.is_valid():
            print(form.errors)

    context = {'form': form}
    return render(request, 'register.html', context)



def loginPage(request):
    context = {}
    return render(request, 'login.html', context)







