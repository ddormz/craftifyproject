# Generated by Django 4.2.5 on 2023-11-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cotizaciones_metodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=19.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizaciones',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cotizaciones',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
