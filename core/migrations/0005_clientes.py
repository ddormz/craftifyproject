# Generated by Django 4.2.5 on 2023-10-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_statusproyecto_proyecto_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rut_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
            ],
        ),
    ]
