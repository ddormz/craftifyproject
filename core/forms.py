from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'groups']
    REQUIRED_FIELDS = ['rut', 'first_name', 'last_name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name']
   

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['id_proyecto', 'cliente', 'categoria', 'nombre_proyecto', 'instalacion', 'fecha', 'plazo_entrega', 'status']

class AgregarProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['id_proyecto', 'cliente', 'categoria', 'nombre_proyecto', 'instalacion', 'fecha', 'plazo_entrega', 'status']

