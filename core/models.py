from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.core.validators import RegexValidator

from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    rut = models.CharField('rut', max_length=10, unique=True, validators=[
        RegexValidator(
            regex='^[0-9kK]+$',
            message='Este campo solo puede contener digitos.',
            code='invalid_name'
        )
    ])
    email = models.EmailField(unique=True)
    token = models.UUIDField(primary_key=False,  editable=False, null=True, blank=True)

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.first_name.capitalize()) + " " + str(self.last_name.capitalize())

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'email'])
        item['rut'] = self.rut
        item['first_name'] = self.first_name
        item['last_name'] = self.last_name
        return item
    
    def has_view_clientes_permission(self):
        return self.has_perm('core.view_clientes')
    def has_view_proyectos_permission(self):
        return self.has_perm('core.view_proyecto')
    def has_view_cotizaciones_permission(self):
        return self.has_perm('core.view_cotizaciones')
    def has_view_avances_permission(self):
        return self.has_perm('core.view_avances')
    def has_view_tareas_permission(self):
        return self.has_perm('core.view_tareas')
    def has_view_equipos_permission(self):
        return self.has_perm('core.view_equipos')
    def has_view_productos_permission(self):
        return self.has_perm('core.view_productos')



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
        item['nombre'] = self.nombre
        item['apellido'] = self.apellido
        item['rut_cliente'] = self.rut_cliente
        item['direccion'] = self.direccion
        return item
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey('Cotizaciones', on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE, null=True, blank=True, default=0)
    categoria = models.ForeignKey('CategoriaProyecto', on_delete=models.CASCADE, default=1)
    nombre_proyecto = models.CharField(max_length=100)
    instalacion = models.BooleanField(default=False)
    fecha = models.DateField(default=datetime.now)
    plazo_entrega = models.DateField()
    status = models.ForeignKey('StatusProyecto', on_delete=models.CASCADE, default=1)
  
    def __str__(self):
        return str(self.nombre_proyecto) + str(" - ") + str(self.cliente)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['nombre_proyecto'] = self.nombre_proyecto
        item['id_cotizacion'] = self.id_cotizacion.toJSON()
        return item

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
    id_status_p = models.AutoField(primary_key=True)
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
    observaciones = models.TextField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.nombre_equipo)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['proyecto_id_proyecto'] = self.proyecto_id_proyecto.toJSON()
        item['nombre_equipo'] = self.nombre_equipo
        item['id_equipo'] = self.id_equipo
        item['observaciones'] = self.observaciones
        item['detalle'] = [i.toJSON() for i in self.detalleequipo_set.all()]
        return item


    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['nombre_equipo']




class DetalleEquipo(models.Model):
    id_Detalle = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey('Equipos', on_delete=models.CASCADE)
    trabajador = models.ForeignKey('User', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_equipo.nombre_equipo) + str(" - ") + str(self.trabajador.first_name) + str("  ") + str(self.trabajador.last_name)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['trabajador'] = self.trabajador.toJSON()
        return item

    class Meta:
        verbose_name = 'Detalle de Equipo'
        verbose_name_plural = 'Detalle de Equipos'
        ordering = ['id_equipo']

    
    
class StatusTarea(models.Model):
    id_status_tarea = models.AutoField(primary_key=True)
    nombre_status = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_status)
    

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Status de Tarea'
        verbose_name_plural = 'Status de Tareas'
        ordering = ['nombre_status']


class Tareas(models.Model):
    tarea_id = models.AutoField(primary_key=True)
    equipo_id_equipo = models.ForeignKey('Equipos', on_delete=models.CASCADE)
    trabajador = models.ForeignKey('User', on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(default=datetime.now)
    fecha_termino = models.DateField()
    tarea = models.TextField(max_length=100)
    status_tarea = models.ForeignKey('StatusTarea', on_delete=models.CASCADE, default=1)
    def __str__(self):
        return str('Equipo: ') +  str(self.equipo_id_equipo) + str(" - ") + str(" Proyecto: ") + str(self.equipo_id_equipo.proyecto_id_proyecto.nombre_proyecto) + str(" - ") + str(' Tarea: ') + str(self.tarea)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['equipo_id_equipo'] = self.equipo_id_equipo.toJSON()
        item['trabajador'] = self.trabajador.toJSON()
        item['status_tarea'] = self.status_tarea.toJSON()
        return item
    
    @staticmethod
    def trabajadores_por_equipo(equipo_id):
        """
        Obtener la lista de trabajadores asociados a un equipo específico.
        """
        return User.objects.filter(detalleequipo__id_equipo=equipo_id)

    class Meta:
        verbose_name = 'Tarea de Equipo'
        verbose_name_plural = 'Tareas de Equipos'
        ordering = ['fecha_asignacion']
    
class Avances(models.Model):
    avance_id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='avances')
    fecha = models.DateTimeField(default=datetime.now)
    comentario = models.TextField(max_length=100)
    tarea = models.ForeignKey('Tareas', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.avance_id) + str(" - ") + str(self.comentario)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['tarea'] = self.tarea.toJSON()
        item['imagen'] = self.imagen.url
        return item
    
    class Meta:
        verbose_name = 'Avance'
        verbose_name_plural = 'Avances'
        ordering = ['avance_id']

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.ForeignKey('CategoriaProductos', on_delete=models.CASCADE, default=1)
    subcategoria = models.ForeignKey('SubcategoriaProductos', on_delete=models.CASCADE, default=1)
    marca = models.ForeignKey('MarcaProductos', on_delete=models.CASCADE, default=1)
    precio_compra = models.FloatField(default=0)
    precio_venta = models.FloatField(default=0)
    variante = models.CharField(max_length=100, null=True, blank=True)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    def __str__(self):
        return str(self.nombre_producto) + str(" - ") + str(self.variante)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['categoria'] = self.categoria.toJSON()
        item['precio_venta'] = format(self.precio_venta, '.0f')
        item['subcategoria'] = self.subcategoria.toJSON()
        item['marca'] = self.marca.toJSON()
        if self.imagen:
            item['imagen'] = self.imagen.url
        else:
            item['imagen'] = '/core/static/img/default.jpg'        
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
    
    
class Cotizaciones(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    fecha_cotizacion = models.DateField(default=datetime.now)
    nombre_cotizacion = models.CharField(max_length=100, null=True, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=60, decimal_places=2)
    iva = models.DecimalField(default=19.00, max_digits=60, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=60, decimal_places=2)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    generado_por = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.TextField(max_length=1000, null=True, blank=True)
    metodopago = models.ForeignKey('MetodoPago', on_delete=models.CASCADE)
    status = models.ForeignKey('StatusCotizacion', on_delete=models.CASCADE)

    def __str__(self):
        return '#' + str(self.id_cotizacion) + ' - '+  str(self.nombre_cotizacion)
    

    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['nombre_cotizacion'] = self.nombre_cotizacion
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['fecha_cotizacion'] = self.fecha_cotizacion.strftime('%Y-%m-%d')
        item['comentario'] = self.comentario
        item['metodopago'] = self.metodopago.toJSON()
        item['det'] = [i.toJSON() for i in self.detallecotizaciones_set.all()]
        item['status'] = self.status.toJSON()
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


class MetodoPago(models.Model):
    id_metodopago = models.AutoField(primary_key=True)
    nombre_metodo = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_metodo)
    
    def toJSON(self):
        item = model_to_dict(self)
        nombre_metodo = self.nombre_metodo
        return item
    
class StatusCotizacion(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_status = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_status)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item