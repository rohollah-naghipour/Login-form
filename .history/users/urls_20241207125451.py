from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage ,name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('login/Home/', views.homepage, name = 'home'),
]
