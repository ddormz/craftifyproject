# Generated by Django 4.2.5 on 2023-11-11 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_productos_id_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='avances',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
