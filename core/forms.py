from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout  
from crispy_forms.layout import Field


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff']
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

class editarTrabajadorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name','email','groups']
    REQUIRED_FIELDS = ['rut','first_name', 'last_name','email','groups']



class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = "__all__"

class AgregarProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = "__all__"
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'plazo_entrega': forms.DateInput(attrs={'type': 'date'}),
            "nombre_proyecto" : forms.TextInput(attrs={'placeholder': 'Ej. Mesita'})
        }

    def __init__(self, *args, **kwargs):
            super(AgregarProyectoForm, self).__init__(*args, **kwargs)
            self.fields['cliente'].label = "Cliente Proyecto"
            self.fields['categoria'].label = "Categoria Proyecto"
            self.fields['nombre_proyecto'].label = "Nombre del Proyecto"
            self.fields['fecha'].label = "Fecha de Creación"
            self.fields['plazo_entrega'].label = "Fecha de Entrega"
            self.fields['status'].label = "Status del Proyecto"
            self.fields['instalacion'].label = "¿Desea Instalación?"
      



class CotizacionesForm(forms.ModelForm):

    class Meta:
        model = Cotizaciones
        fields = "__all__"
        widgets = {
            'nombre_cotizacion': forms.TextInput(attrs={'placeholder': 'Ej. Cocina'}),
            'fecha_cotizacion': forms.DateTimeInput(attrs={'type': 'date'}),
            'iva': forms.NumberInput(attrs={"disabled": True}),
            'total': forms.NumberInput(attrs={"disabled": True}),
            'subtotal': forms.NumberInput(attrs={"disabled": True}),
            'fecha_cotizacion': forms.DateTimeInput(
                {
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha_cotizacion',
                    'data-target': '#fecha_cotizacion',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'cliente': forms.Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),};
    def __init__(self, *args, **kwargs):
        super(CotizacionesForm, self).__init__(*args, **kwargs)
        self.fields['fecha_cotizacion'].label = "Fecha de Cotización"
        self.fields['iva'].label = "IVA (%)"
        self.fields['total'].label = "Monto Total"
        self.fields['subtotal'].label = "Monto Neto"
        self.fields['cliente'].label = "Seleccionar Cliente"
        self.fields['nombre_cotizacion'].label = "Nombre de Cotización"


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"


class CatForm(forms.ModelForm):
    class Meta:
        model = CategoriaProductos
        fields = "__all__"

class SubCatForm(forms.ModelForm):
    class Meta:
        model = SubcategoriaProductos
        fields = "__all__"

class AvanceForm(forms.ModelForm):
    class Meta:
        model = Avances
        fields = "__all__"


class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = "__all__"


class AsignacionForm(forms.ModelForm):
    class Meta:
        model = EquipoAsignacion
        fields = "__all__"
        widgets = {
            'tiempo_asignado': forms.DateInput(attrs={'type': 'date'}),
            'tiempo_final': forms.DateInput(attrs={'type': 'date'}),
        }