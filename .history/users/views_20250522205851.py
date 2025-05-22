from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .form import UserRegistrationForm, UserLoginForm 

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username,
                                             email=email,
                                               password=password)
            user.save()
            return redirect('login') 
        else:
            pass 
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, 
                                username=username,
                                  password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Welcome, {username}!')
                return redirect('home') 
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)

def homePage(request):
    return render(request, 'home.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login') 



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

