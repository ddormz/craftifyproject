from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout  
from crispy_forms.layout import Field
from django.core.validators import RegexValidator

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
            'iva': forms.NumberInput(attrs={"disabled": True, "value": 19}),
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
    telefono = forms.IntegerField()
    nombre = forms.CharField(max_length=100, validators=[
        RegexValidator(
            regex='^[a-zA-Z ]+$',  # Modificado para permitir espacios
            message='Este campo solo puede contener letras.',
            code='invalid_name'
        )
    ])
    apellido = forms.CharField(max_length=100, validators=[
        RegexValidator(
            regex='^[a-zA-Z ]+$',  # Modificado para permitir espacios
            message='Este campo solo puede contener letras.',
            code='invalid_name'
        )
    ])
    rut_cliente = forms.CharField(max_length=10, validators=[
        RegexValidator(
            regex='^[0-9kK]+$',
            message='Este campo solo puede contener digitos.',
            code='invalid_name'

        )
    ])
    

    class Meta:
        model = Clientes
        fields = ['rut_cliente', 'nombre', 'apellido', 'direccion', 'telefono']


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"
        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = MarcaProductos
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'accept': 'image/*'})  # Esto permite seleccionar solo archivos de imagen


class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = "__all__"
        widgets = {
            'proyecto_id_proyecto': forms.Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'nombre_equipo': forms.TextInput(attrs={
                'placeholder': 'Ej. Producción'
            })
        }


    def __init__(self, *args, **kwargs):
        super(EquiposForm, self).__init__(*args, **kwargs)
        self.fields['nombre_equipo'].label = "Nombre del Equipo"
        self.fields['proyecto_id_proyecto'].label = "Nombre Proyecto"


class TareasForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = "__all__"
        widgets = {
            'fecha_asignacion': forms.DateInput(attrs={'type': 'date', }),
            'fecha_termino': forms.DateInput(attrs={'type': 'date', }),
        }
  
    def __init__(self, *args, **kwargs):
        super(TareasForm, self).__init__(*args, **kwargs)
        self.fields['fecha_asignacion'].label = "Fecha de Asignación"
        self.fields['fecha_termino'].label = "Fecha de Terminación"
        self.fields['equipo_id_equipo'].label = "Equipo"
        self.fields['trabajador'].label = "Trabajador"
        self.fields['tarea'].label = "Tarea"
        

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['rut', 'password']


class CategoriaProyectoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProyecto
        fields = ['nombre_categoria']


class StatusProyectoForm(forms.ModelForm):
    class Meta:
        model = StatusProyecto
        fields = ['nombre_status']

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre_metodo']


class StatusTareaForm(forms.ModelForm):
    class Meta:
        model = StatusTarea
        fields = ['nombre_status']