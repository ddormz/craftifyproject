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
        fields = ['rut', 'first_name', 'last_name', 'email', 'password1', 'password2','groups']
        widgets = {
            'groups': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple',
            })
        }

        rut = forms.CharField(max_length=10, validators=[
            RegexValidator(
                regex='^[0-9kK]+$',
                message='Este campo solo puede contener digitos.',
                code='invalid_name'

            )
        ])
        first_name = forms.CharField(max_length=100, validators=[
            RegexValidator(
                regex='^[a-zA-Z ]+$',
                message='Este campo solo puede contener letras.',
                code='invalid_name'
            )
        ])
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['rut'].help_text = 'Ingrese el RUT sin puntos ni guion, si termina en K reemplace por 0.'
        self.fields['groups'].label = "Rol y Permisos"
        self.fields['first_name'].help_text = 'Ingrese el Nombre solo con letras.'
        self.fields['last_name'].help_text = 'Ingrese el Apellido solo con letras.'
        self.fields['email'].help_text = 'Ingrese un correo electronico valido.'
        self.fields['email'].label = "Correo Electronico"
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = 'Debe contener al menos 8 caracteres y no puede contener información personal.'

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
            'fecha': forms.DateInput(
                attrs={
                    'type': 'date',
                    'value': datetime.now().strftime('%Y-%m-%d')

                }
            ),
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
            self.fields['id_cotizacion'].label = "Seleccione Cotización"
      



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
    class Meta:
        model = Clientes
        fields = ['rut_cliente', 'nombre', 'apellido', 'direccion', 'telefono']
        widgets = {
            'rut_cliente': forms.TextInput(attrs={'placeholder': 'Ej. 12345678-9'}),
        }

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'accept': 'image/*'})

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            # Asegúrate de que la imagen no sea demasiado grande, etc.
            # Puedes agregar validaciones personalizadas aquí según tus requisitos.
            pass
        return imagen 

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


# Formulario
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

class StatusCotizacionForm(forms.ModelForm):
    class Meta:
        model = StatusCotizacion
        fields = ['nombre_status']



class ResetPasswordForm(forms.Form):
    rut = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su RUT'}), max_length=10, validators=[
        RegexValidator(
            regex='^[0-9kK]+$',
            message='Este campo solo puede contener digitos.',
            code='invalid_name'

        )
    ])

    def clean_rut(self):
        cleaned = super().clean()
        if not User.objects.filter(rut=cleaned['rut']).exists():
            raise forms.ValidationError('El RUT no existe')
        return cleaned['rut']

    def get_user(self):
        rut = self.cleaned_data['rut']
        return User.objects.get(rut=rut)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese un password',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita el password',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        password = cleaned['password']
        confirmPassword = cleaned['confirmPassword']
        if password != confirmPassword:
            # self._errors['error'] = self._errors.get('error', self.error_class())
            # self._errors['error'].append('El usuario no existe')
            raise forms.ValidationError('Las contraseñas deben ser iguales')
        return cleaned