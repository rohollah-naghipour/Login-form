from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'email', 'password']

        


