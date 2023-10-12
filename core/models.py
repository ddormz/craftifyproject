from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    rut = models.CharField('rut', max_length=10, unique=True)

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.rut


class Clientes(models.Model):
    rut_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    def __str__(self):
        return str(self.rut_cliente) + str(" ") + str(self.nombre) + str(" ") + str(self.apellido)

class Proyecto(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey('CategoriaProyecto', on_delete=models.CASCADE)
    nombre_proyecto = models.CharField(max_length=100)
    instalacion = models.BooleanField(default=False)
    fecha = models.DateField(blank=True, null=True)
    plazo_entrega = models.DateField()
    status = models.ForeignKey('StatusProyecto', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre_proyecto)

class CategoriaProyecto(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_categoria)

class StatusProyecto(models.Model):
    id_status = models.IntegerField(primary_key=True)
    nombre_status = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_status)
    
class Equipos(models.Model):
    proyecto_id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    id_equipo = models.IntegerField(primary_key=True)
    nombre_equipo = models.CharField(max_length=100)
    trabajadores = models.ForeignKey('User', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_equipo) + str(self.nombre_equipo)
    
class EquipoAsignacion(models.Model):
    asignacion_id = models.IntegerField(primary_key=True)
    equipo_id_equipo = models.ForeignKey('Equipos', on_delete=models.CASCADE)
    proyecto_id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    tiempo_asignado = models.DateField()
    tiempo_final = models.DateField()
    def __str__(self):
        return str(self.equipo_id_equipo) + str(self.proyecto_id_proyecto)
    
class Avances(models.Model):
    avance_id = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to='avances')
    comentario = models.CharField(max_length=45)
    asignacion_asignacion = models.ForeignKey('EquipoAsignacion', on_delete=models.CASCADE)
    equipo_id_equipo = models.ForeignKey('Equipos', on_delete=models.CASCADE)
    proyecto_id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.avance_id)
    

class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey('CategoriaProductos', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey('SubcategoriaProductos', on_delete=models.CASCADE)
    marca = models.ForeignKey('MarcaProductos', on_delete=models.CASCADE)
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    variante = models.ForeignKey('VarianteProductos', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.id_producto) + str(self.nombre_producto)


class CategoriaProductos(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_categoria)
    
class SubcategoriaProductos(models.Model):
    id_subcategoria = models.IntegerField(primary_key=True)
    nombre_subcategoria = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_subcategoria)
    
class MarcaProductos(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre_marca = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_marca)
    
class VarianteProductos(models.Model):
    id_variante = models.IntegerField(primary_key=True)
    nombre_variante = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_variante)
    
class Cotizaciones(models.Model):
    id_cotizacion = models.IntegerField(primary_key=True)
    fecha_cotizacion = models.DateField()
    nombre_cotizacion = models.CharField(max_length=100)
    total_neto = models.IntegerField()
    total_impuestos = models.IntegerField()
    total = models.IntegerField()
    detalle = models.ForeignKey('DetalleCotizaciones', on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    generado_por = models.ForeignKey('User', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_cotizacion) + str(self.nombre_cotizacion)
    
class DetalleCotizaciones(models.Model):
    id_cotizacion = models.ForeignKey('Cotizaciones', on_delete=models.CASCADE, null=True, blank=True)
    id_producto = models.ForeignKey('Productos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return str(self.id_cotizacion) + str(self.id_producto)