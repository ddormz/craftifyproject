# Generated by Django 4.2.5 on 2023-11-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_equipos_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='observaciones',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
