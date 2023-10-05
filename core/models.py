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
        return str(self.rut_cliente) + str(self.nombre)

class Proyecto(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey('CategoriaProyecto', on_delete=models.CASCADE, null=True)
    nombre_proyecto = models.CharField(max_length=100)
    instalacion = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)
    plazo_entrega = models.DateField()
    status = models.ForeignKey('StatusProyecto', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id_proyecto) + str(self.nombre_proyecto)  + self.status.nombre_status

class CategoriaProyecto(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id_categoria) + str(self.nombre_categoria)
    
class StatusProyecto(models.Model):
    id_status = models.IntegerField(primary_key=True)
    nombre_status = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id_status) + str(self.nombre_status)
    
