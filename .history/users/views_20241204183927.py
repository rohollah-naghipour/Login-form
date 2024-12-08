from django.shortcuts import redirect
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
        print("OKKKKKKKKKKKKKKKKKKKKKKKKK")
        if form.is_valid():
            form.save()
            print("user created OK 200 ")
            return redirect('login')
      
    template = loader.get_template('register.html')   
    context = {
        'form': form
    }                 
    return HttpResponse(template.render(context, request))

      #if not form.is_valid():
            #print(form.errors)
    #context = {'form': form}
    #return render(request, 'register.html', context)


def loginPage(request):
    template = loader.get_template('login.html')   
    context = {}                 
    return HttpResponse(template.render(context, request))







