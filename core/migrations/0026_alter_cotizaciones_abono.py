# Generated by Django 4.2.7 on 2024-03-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_clientes_comuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='abono',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
