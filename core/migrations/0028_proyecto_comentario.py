# Generated by Django 4.2.7 on 2024-06-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_cotizaciones_abono'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='comentario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]