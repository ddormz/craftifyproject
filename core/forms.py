from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

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
        fields = ['id_proyecto', 'cliente', 'categoria', 'nombre_proyecto', 'instalacion', 'fecha', 'plazo_entrega', 'status']

class AgregarProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['id_proyecto', 'cliente', 'categoria', 'nombre_proyecto', 'instalacion', 'fecha', 'plazo_entrega', 'status']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'plazo_entrega': forms.DateInput(attrs={'type': 'date'}),
            "nombre_proyecto" : forms.TextInput(attrs={'placeholder': 'Ej. Mesita'})
        }

    def __init__(self, *args, **kwargs):
            super(AgregarProyectoForm, self).__init__(*args, **kwargs)
            self.fields['id_proyecto'].label = "ID Proyecto"
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
        fields = ['id_cotizacion','fecha_cotizacion','nombre_cotizacion','total_neto', 'total_impuestos', 'total', 'detalle', 'cliente', 'generado_por']
        widgets = {
            'fecha_cotizacion': forms.DateTimeInput(attrs={'type': 'date'}),
        }


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['rut_cliente', 'nombre', 'apellido', 'direccion', 'telefono']


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['id_producto', 'nombre_producto','descripcion', 'categoria', 'subcategoria', 'marca', 'precio_compra', 'precio_venta', 'variante']


class CatForm(forms.ModelForm):
    class Meta:
        model = CategoriaProductos
        fields = ['id_categoria', 'nombre_categoria']

class SubCatForm(forms.ModelForm):
    class Meta:
        model = SubcategoriaProductos
        fields = ['id_subcategoria', 'nombre_subcategoria']

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