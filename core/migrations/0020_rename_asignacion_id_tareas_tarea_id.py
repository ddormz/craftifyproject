# Generated by Django 4.2.5 on 2023-11-05 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_detalleequipo_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='asignacion_id',
            new_name='tarea_id',
        ),
    ]