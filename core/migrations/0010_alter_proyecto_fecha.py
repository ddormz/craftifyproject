# Generated by Django 4.2.5 on 2023-10-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_proyecto_status_delete_statusporproyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
