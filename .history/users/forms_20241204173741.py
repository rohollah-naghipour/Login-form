from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = '__all__'
        #['username', 'email', 'password1', 'password2']




