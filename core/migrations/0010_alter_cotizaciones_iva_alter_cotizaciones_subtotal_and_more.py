# Generated by Django 4.2.5 on 2023-11-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_productos_precio_compra_and_more'),
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
        migrations.AlterField(
            model_name='detallecotizaciones',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio_compra',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio_venta',
            field=models.FloatField(default=0),
        ),
    ]