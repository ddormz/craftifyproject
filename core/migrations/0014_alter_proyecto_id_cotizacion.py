# Generated by Django 4.2.5 on 2023-11-27 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_proyecto_id_cotizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='id_cotizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cotizaciones'),
        ),
    ]
