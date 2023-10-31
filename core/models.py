from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext_lazy as _
from datetime import datetime

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
    telefono = models.CharField(max_length=11)
    def __str__(self):
        return str(self.nombre) + str(" ") + str(self.apellido)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE, null=True, blank=True, default=0)
    categoria = models.ForeignKey('CategoriaProyecto', on_delete=models.CASCADE, default=1)
    nombre_proyecto = models.CharField(max_length=100)
    instalacion = models.BooleanField(default=False)
    fecha = models.DateField(default=datetime.now)
    plazo_entrega = models.DateField()
    status = models.ForeignKey('StatusProyecto', on_delete=models.CASCADE, default=1)
  
    def __str__(self):
        return str(self.nombre_proyecto) + str(" - ") + str(self.cliente)
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id_proyecto']

class CategoriaProyecto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_categoria)
    
    class Meta:
        verbose_name = 'Categoría de Proyecto'
        verbose_name_plural = 'Categorias de Proyectos'
        ordering = ['nombre_categoria']

class StatusProyecto(models.Model):
    id_status = models.AutoField(primary_key=True)
    nombre_status = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_status)
    
    class Meta:
        verbose_name = 'Status de Proyecto'
        verbose_name_plural = 'Status de Proyectos'
        ordering = ['nombre_status']
    
class Equipos(models.Model):
    proyecto_id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    id_equipo = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=100)
    trabajadores = models.ForeignKey('User', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre_equipo)
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['nombre_equipo']
    

class EquipoAsignacion(models.Model):
    asignacion_id = models.AutoField(primary_key=True)
    equipo_id_equipo = models.ForeignKey('Equipos', on_delete=models.CASCADE)
    proyecto_id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(default=datetime.now)
    fecha_termino = models.DateField()
    tarea = models.CharField(max_length=100)
    def __str__(self):
        return str('Equipo: ') +  str(self.equipo_id_equipo) + str(" - ") + str(self.tarea)
    
    class Meta:
        verbose_name = 'Tarea de Equipo'
        verbose_name_plural = 'Tareas de Equipos'
        ordering = ['fecha_asignacion']
    
class Avances(models.Model):
    avance_id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='avances')
    comentario = models.CharField(max_length=100)
    asignacion_asignacion = models.ForeignKey('EquipoAsignacion', on_delete=models.CASCADE, null=True, blank=True)
    equipo_id_equipo = models.ForeignKey('Equipos', on_delete=models.CASCADE, null=True, blank=True)
    proyecto_id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.avance_id) + str(" - ") + str(self.comentario)
    
    class Meta:
        verbose_name = 'Avance'
        verbose_name_plural = 'Avances'
        ordering = ['avance_id']

class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey('CategoriaProductos', on_delete=models.CASCADE, default=1)
    subcategoria = models.ForeignKey('SubcategoriaProductos', on_delete=models.CASCADE, default=1)
    marca = models.ForeignKey('MarcaProductos', on_delete=models.CASCADE, default=1)
    precio_compra = models.FloatField(default=0)
    precio_venta = models.FloatField(default=0)
    variante = models.ForeignKey('VarianteProductos', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.nombre_producto) + str(" - ") + str(self.variante)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['categoria'] = self.categoria.toJSON()
        item['precio_venta'] = format(self.precio_venta, '.2f')
        item['variante'] = self.variante.toJSON()
        item['subcategoria'] = self.subcategoria.toJSON()
        return item
    

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id_producto']

class CategoriaProductos(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_categoria)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'
        ordering = ['nombre_categoria']
    
class SubcategoriaProductos(models.Model):
    id_subcategoria = models.AutoField(primary_key=True)
    nombre_subcategoria = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_subcategoria)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Subcategoría de Producto'
        verbose_name_plural = 'Subcategorías de Productos'
        ordering = ['nombre_subcategoria']
    
class MarcaProductos(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_marca)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Marca de Producto'
        verbose_name_plural = 'Marcas de Productos'
        ordering = ['nombre_marca']
    
class VarianteProductos(models.Model):
    id_variante = models.AutoField(primary_key=True)
    nombre_variante = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_variante)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Variante de Producto'
        verbose_name_plural = 'Variantes de Productos'
        ordering = ['nombre_variante']
    
class Cotizaciones(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    fecha_cotizacion = models.DateField(default=datetime.now)
    nombre_cotizacion = models.CharField(max_length=100, null=True, blank=True)
    subtotal = models.FloatField(default=0)
    iva = models.IntegerField(default=19)
    total = models.FloatField(default=0)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    generado_por = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.TextField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return str(self.id_cotizacion) + str(self.nombre_cotizacion)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['nombre_cotizacion'] = self.nombre_cotizacion
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['fecha_cotizacion'] = self.fecha_cotizacion.strftime('%Y-%m-%d')
        item['comentario'] = self.comentario
        item['det'] = [i.toJSON() for i in self.detallecotizaciones_set.all()]
        return item

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        ordering = ['id_cotizacion']

    
class DetalleCotizaciones(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey('Cotizaciones', on_delete=models.CASCADE)
    producto = models.ForeignKey('Productos', on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    subtotal = models.FloatField(default=0)
    def __str__(self):
        return str(self.id_cotizacion) + str(self.producto)
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['id_cotizacion'])
        item['producto'] = self.producto.toJSON()
        item['precio'] = format(self.precio, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Cotización'
        verbose_name_plural = 'Detalles de Cotizaciones'
        ordering = ['id_cotizacion']

