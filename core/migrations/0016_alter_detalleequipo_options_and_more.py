# Generated by Django 4.2.5 on 2023-11-04 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_detalleequipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalleequipo',
            options={'ordering': ['equipo_id_equipo'], 'verbose_name': 'Detalle de Equipo', 'verbose_name_plural': 'Detalle de Equipos'},
        ),
        migrations.RemoveField(
            model_name='equipos',
            name='trabajadores',
        ),
    ]
