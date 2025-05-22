from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage ,name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('home/', views.homepage, name = 'home'),
   
]
# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('home/', views.homePage, name='home'), # Assuming you have a homepage view
]