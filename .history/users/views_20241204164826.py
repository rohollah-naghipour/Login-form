from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .forms import *


def registerPage(request):
    context = {}
    return render(request, 'register.html', context)



def loginPage(request):
    context = {}
    return render(request, 'login.html', context)







