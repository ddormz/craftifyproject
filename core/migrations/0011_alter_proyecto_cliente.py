# Generated by Django 4.2.5 on 2023-10-05 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_proyecto_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.clientes'),
        ),
    ]
