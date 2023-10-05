from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'groups']


class UserForm(UserCreationForm):
    class Meta:
        fields = ['rut', 'first_name', 'last_name']
        model = User