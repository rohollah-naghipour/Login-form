from django.urls import path
from .views import registerPage, loginPage
urlpatterns = [
    path('', views.registerPage ,name = 'register'),

]


from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]