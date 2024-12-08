from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.csrf import csrf_protect

from .models import User
from .forms import *

@csrf_protect
def registerPage(request):
    form = UserCreationForm()

    if request == 'POST':
        user = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render_to_response('register.html', csrf_protect)
    #return render(request, 'register.html', context)




def loginPage(request):
    context = {}
    return render(request, 'login.html', context)







