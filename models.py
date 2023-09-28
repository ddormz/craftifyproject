# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Avances(models.Model):
    avance_id = models.IntegerField(primary_key=True)  # The composite primary key (avance_id, asignacion_asignacion_id, asignacion_equipo_id_equipo, asignacion_equipo_proyectos_id_proyecto) found, that is not supported. The first column is selected.
    imagen = models.TextField(blank=True, null=True)
    comentario = models.CharField(max_length=45, blank=True, null=True)
    asignacion_asignacion = models.ForeignKey('EquipoAsignacion', models.DO_NOTHING)
    asignacion_equipo_id_equipo = models.ForeignKey('EquipoAsignacion', models.DO_NOTHING, db_column='asignacion_equipo_id_equipo', to_field='equipo_id_equipo', related_name='avances_asignacion_equipo_id_equipo_set')
    asignacion_equipo_proyectos_id_proyecto = models.ForeignKey('EquipoAsignacion', models.DO_NOTHING, db_column='asignacion_equipo_proyectos_id_proyecto', to_field='equipo_proyectos_id_proyecto', related_name='avances_asignacion_equipo_proyectos_id_proyecto_set')

    class Meta:
        managed = False
        db_table = 'avances'
        unique_together = (('avance_id', 'asignacion_asignacion', 'asignacion_equipo_id_equipo', 'asignacion_equipo_proyectos_id_proyecto'),)


class CotCategoriaProductos(models.Model):
    categoria_id = models.IntegerField(primary_key=True)  # The composite primary key (categoria_id, subcategoria_id_subcategoria) found, that is not supported. The first column is selected.
    nombre_categoria = models.CharField(max_length=45, blank=True, null=True)
    subcategoria_id_subcategoria = models.ForeignKey('CotSubcategoria', models.DO_NOTHING, db_column='subcategoria_id_subcategoria')

    class Meta:
        managed = False
        db_table = 'cot_categoria_productos'
        unique_together = (('categoria_id', 'subcategoria_id_subcategoria'),)


class CotClientes(models.Model):
    rut_cliente = models.IntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=45)
    apellido_cliente = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cot_clientes'


class CotDetCot(models.Model):
    cotizaciones_id_cotizacion = models.OneToOneField('Cotizaciones', models.DO_NOTHING, db_column='cotizaciones_id_cotizacion', primary_key=True)  # The composite primary key (cotizaciones_id_cotizacion, productos_producto_id) found, that is not supported. The first column is selected.
    productos_producto = models.ForeignKey('CotProductos', models.DO_NOTHING)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cot_det_cot'
        unique_together = (('cotizaciones_id_cotizacion', 'productos_producto'),)


class CotMarca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre_marca = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cot_marca'


class CotProductos(models.Model):
    producto_id = models.IntegerField(primary_key=True)
    precio_unitario = models.FloatField()
    nombre_producto = models.CharField(max_length=45)
    categoria_productos_categoria = models.ForeignKey(CotCategoriaProductos, models.DO_NOTHING)
    categoria_productos_subcategoria_id_subcategoria = models.ForeignKey(CotCategoriaProductos, models.DO_NOTHING, db_column='categoria_productos_subcategoria_id_subcategoria', to_field='subcategoria_id_subcategoria', related_name='cotproductos_categoria_productos_subcategoria_id_subcategoria_set')
    marca_id_marca = models.ForeignKey(CotMarca, models.DO_NOTHING, db_column='marca_id_marca')
    variante_id_variante = models.ForeignKey('CotVariante', models.DO_NOTHING, db_column='variante_id_variante')

    class Meta:
        managed = False
        db_table = 'cot_productos'


class CotSubcategoria(models.Model):
    id_subcategoria = models.IntegerField(primary_key=True)
    nombre_subcategoria = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cot_subcategoria'


class CotVariante(models.Model):
    id_variante = models.IntegerField(primary_key=True)
    nombre_variante = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cot_variante'


class Cotizaciones(models.Model):
    id_cotizacion = models.IntegerField(primary_key=True)  # The composite primary key (id_cotizacion, trabajador_rut_trabajador) found, that is not supported. The first column is selected.
    fecha = models.DateTimeField(blank=True, null=True)
    total_neto = models.FloatField()
    iva = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    cliente_rut_cliente = models.ForeignKey(CotClientes, models.DO_NOTHING, db_column='cliente_rut_cliente')
    trabajador_rut_trabajador = models.ForeignKey('CuentasTrabajador', models.DO_NOTHING, db_column='trabajador_rut_trabajador')

    class Meta:
        managed = False
        db_table = 'cotizaciones'
        unique_together = (('id_cotizacion', 'trabajador_rut_trabajador'),)


class CuentasRoles(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=45)
    nivel_privilegio = models.IntegerField()
    cuentas_trabajador_rut_trabajador = models.ForeignKey('CuentasTrabajador', models.DO_NOTHING, db_column='cuentas_trabajador_rut_trabajador')

    class Meta:
        managed = False
        db_table = 'cuentas_roles'


class CuentasTrabajador(models.Model):
    rut_trabajador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    rol_id = models.IntegerField()
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cuentas_trabajador'


class Equipo(models.Model):
    id_equipo = models.IntegerField(primary_key=True)  # The composite primary key (id_equipo, proyectos_id_proyecto) found, that is not supported. The first column is selected.
    proyectos_id_proyecto = models.ForeignKey('Proyectos', models.DO_NOTHING, db_column='proyectos_id_proyecto')
    nombre_equipo = models.CharField(max_length=45, blank=True, null=True)
    trabajador_rut = models.ForeignKey(CuentasTrabajador, models.DO_NOTHING, db_column='trabajador_rut')

    class Meta:
        managed = False
        db_table = 'equipo'
        unique_together = (('id_equipo', 'proyectos_id_proyecto'),)


class EquipoAsignacion(models.Model):
    asignacion_id = models.IntegerField(primary_key=True)  # The composite primary key (asignacion_id, equipo_id_equipo, equipo_proyectos_id_proyecto) found, that is not supported. The first column is selected.
    equipo_id_equipo = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='equipo_id_equipo')
    equipo_proyectos_id_proyecto = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='equipo_proyectos_id_proyecto', to_field='proyectos_id_proyecto', related_name='equipoasignacion_equipo_proyectos_id_proyecto_set')
    tiempo_asignado = models.DateField(blank=True, null=True)
    tiempo_final = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo_asignacion'
        unique_together = (('asignacion_id', 'equipo_id_equipo', 'equipo_proyectos_id_proyecto'),)


class Materiales(models.Model):
    id_material = models.IntegerField(primary_key=True)
    nombre_material = models.CharField(max_length=45, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    materialescol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiales'


class MaterialesProyecto(models.Model):
    materiales_id_material = models.OneToOneField(Materiales, models.DO_NOTHING, db_column='materiales_id_material', primary_key=True)  # The composite primary key (materiales_id_material, asignacion_asignacion_id, asignacion_equipo_id_equipo, asignacion_equipo_proyectos_id_proyecto) found, that is not supported. The first column is selected.
    asignacion_asignacion = models.ForeignKey(EquipoAsignacion, models.DO_NOTHING)
    asignacion_equipo_id_equipo = models.ForeignKey(EquipoAsignacion, models.DO_NOTHING, db_column='asignacion_equipo_id_equipo', to_field='equipo_id_equipo', related_name='materialesproyecto_asignacion_equipo_id_equipo_set')
    asignacion_equipo_proyectos_id_proyecto = models.ForeignKey(EquipoAsignacion, models.DO_NOTHING, db_column='asignacion_equipo_proyectos_id_proyecto', to_field='equipo_proyectos_id_proyecto', related_name='materialesproyecto_asignacion_equipo_proyectos_id_proyecto_set')
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiales_proyecto'
        unique_together = (('materiales_id_material', 'asignacion_asignacion', 'asignacion_equipo_id_equipo', 'asignacion_equipo_proyectos_id_proyecto'),)


class ProyCategoriaProyecto(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proy_categoria_proyecto'


class ProyStatus(models.Model):
    idstatus = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proy_status'


class ProyStatusPorProyectos(models.Model):
    proyectos_id_proyecto = models.OneToOneField('Proyectos', models.DO_NOTHING, db_column='proyectos_id_proyecto', primary_key=True)  # The composite primary key (proyectos_id_proyecto, status_idstatus) found, that is not supported. The first column is selected.
    status_idstatus = models.ForeignKey(ProyStatus, models.DO_NOTHING, db_column='status_idstatus')
    fecha = models.DateTimeField(blank=True, null=True)
    observacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proy_status_por_proyectos'
        unique_together = (('proyectos_id_proyecto', 'status_idstatus'),)


class Proyectos(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=45, blank=True, null=True)
    categoria_id_proyecto = models.ForeignKey(ProyCategoriaProyecto, models.DO_NOTHING, db_column='categoria_id_proyecto', blank=True, null=True)
    instalacion = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    plazo_entrega = models.DateField(blank=True, null=True)
    cotizaciones_id_cotizacion = models.ForeignKey(Cotizaciones, models.DO_NOTHING, db_column='cotizaciones_id_cotizacion')

    class Meta:
        managed = False
        db_table = 'proyectos'
