# Generated by Django 4.2.5 on 2023-11-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_statustarea_tareas_trabajador_tareas_status_tarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='observaciones',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
