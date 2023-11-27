from rest_framework import serializers
from core.models import *
  

class CotizacionesSerializer(serializers.ModelSerializer):
    nombre_cliente = serializers.CharField(source='cliente.nombre')
    apellido_cliente = serializers.CharField(source='cliente.apellido')
    metodopago = serializers.CharField(source='metodopago.nombre_metodo')
    class Meta:
        model = Cotizaciones
        fields = ['id_cotizacion', 'fecha_cotizacion', 'nombre_cotizacion', 'subtotal', 'iva', 'total', 'cliente', 'metodopago', 'nombre_cliente', 'apellido_cliente', 'comentario']


class AvancesSerializer(serializers.ModelSerializer):
    tarea = serializers.CharField(source='tarea.tarea')
    equipo = serializers.CharField(source='tarea.equipo_id_equipo')
    proyecto = serializers.CharField(source='tarea.equipo_id_equipo.proyecto_id_proyecto')
    status_tarea = serializers.CharField(source='tarea.status_tarea')
    class Meta:
        model = Avances
        fields = ['avance_id','tarea','fecha','comentario','imagen', 'equipo', 'proyecto', 'status_tarea']

class AddAvancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avances
        fields = ['tarea','fecha','comentario','imagen']

class ProyectosSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nombre_categoria')
    status = serializers.CharField(source='status.nombre_status')
    nombre = serializers.CharField(source='cliente.nombre')
    apellido = serializers.CharField(source='cliente.apellido')
    class Meta:
        model = Proyecto
        fields = ['nombre_proyecto','cliente','categoria','fecha','plazo_entrega','status','instalacion','nombre','apellido']


class TrabajadoresSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='first_name')
    apellido = serializers.CharField(source='last_name')
    fecha_agregado = serializers.CharField(source='date_joined')
    class Meta:
        model = User
        fields = ['rut','nombre','apellido','email','fecha_agregado']

class ProductosSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nombre_categoria')
    subcategoria = serializers.CharField(source='subcategoria.nombre_subcategoria')
    marca = serializers.CharField(source='marca.nombre_marca')

    class Meta:
        model = Productos
        fields = '__all__'



class TareasSerializer(serializers.ModelSerializer):
    status_tarea = serializers.CharField(source='status_tarea.nombre_status')
    equipo_id_equipo = serializers.CharField(source='equipo_id_equipo.nombre_equipo')
    trabajador = serializers.CharField(source='trabajador.first_name')
    apellido_trabajador = serializers.CharField(source='trabajador.last_name')
    proyecto = serializers.CharField(source='equipo_id_equipo.proyecto_id_proyecto')
    class Meta:
        model = Tareas
        fields = ['tarea_id','tarea', 'equipo_id_equipo', 'status_tarea', 'trabajador','apellido_trabajador', 'fecha_asignacion', 'fecha_termino', 'proyecto']

