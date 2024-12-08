from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage ,name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('register/login/Home/', views.homepage, name = 'home'),
    path('register/login/', views.loginPage, name = 'login')
]
