from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'groups']
    

class editarTrabajadorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name','email','groups']
    REQUIRED_FIELDS = ['rut','first_name', 'last_name','email','groups']
   

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['id_proyecto', 'cliente', 'categoria', 'nombre_proyecto', 'instalacion', 'fecha', 'plazo_entrega', 'status']

class AgregarProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['id_proyecto', 'cliente', 'categoria', 'nombre_proyecto', 'instalacion', 'fecha', 'plazo_entrega', 'status']

class CotizacionesForm(forms.ModelForm):
    class Meta:
        model = Cotizaciones
        fields = ['id_cotizacion','fecha_cotizacion','nombre_cotizacion','total_neto', 'total_impuestos', 'total', 'detalle', 'cliente', 'generado_por']