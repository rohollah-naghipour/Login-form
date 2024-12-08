#from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import loader

from .models import User
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()

    if request == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("user created OK 200 ")
            return redirect('login')
        
        if not form.is_valid():
            print(form.errors)
    template = loader.get_template('register.html')   
    context = {
        'form': form
    }                 
    return HttpResponse(template.render(context, request))


def testing2(request):
  mymembers = Member.objects.all().order_by('firstname').values()
  template = loader.get_template('template2.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))



    #context = {'form': form}
    #return render(request, 'register.html', context)




def loginPage(request):
    context = {}
    return render(request, 'login.html', context)







