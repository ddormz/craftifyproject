# Generated by Django 4.2.5 on 2023-11-02 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_metodopago_cotizaciones_metodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='metodopago',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.metodopago'),
            preserve_default=False,
        ),
    ]
