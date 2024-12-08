from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'email', 'password']

def save(self, commit=True):
        User = super(self).save(commit=False)
        User.email = self.cleaned_data['email']
        if commit:
            User.save()
            #return User


