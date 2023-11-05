from rest_framework import serializers
from core.models import *


class CotizacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizaciones
        fields = '__all__'

class DetalleCotizacionSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.CharField(source='producto.nombre_producto')
    class Meta:
        model = DetalleCotizaciones
        fields = ['nombre_producto','precio','cantidad','subtotal','id_cotizacion']




class AvancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avances
        fields = '__all__'

class ProyectosSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nombre_categoria')
    status = serializers.CharField(source='status.nombre_status')
    nombre = serializers.CharField(source='cliente.nombre')
    apellido = serializers.CharField(source='cliente.apellido')
    class Meta:
        model = Proyecto
        fields = ['nombre_proyecto','cliente','categoria','fecha','plazo_entrega','status','instalacion', 'nombre', 'apellido']


class TrabajadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['rut','first_name','last_name','email','date_joined']

class ProductosSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nombre_categoria')
    subcategoria = serializers.CharField(source='subcategoria.nombre_subcategoria')
    marca = serializers.CharField(source='marca.nombre_marca')
    variante = serializers.CharField(source='variante.nombre_variante')

    class Meta:
        model = Productos
        fields = '__all__'

class CategoriaProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProductos
        fields = '__all__'

class SubcategoriaProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcategoriaProductos
        fields = '__all__'

class MarcaProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaProductos
        fields = '__all__'

class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipos
        fields = '__all__'




class VariantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VarianteProductos
        fields = '__all__'

class AsignacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusProyecto
        fields = '__all__'


