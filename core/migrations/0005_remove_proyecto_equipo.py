# Generated by Django 4.2.5 on 2023-10-05 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_proyecto_equipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='equipo',
        ),
    ]
