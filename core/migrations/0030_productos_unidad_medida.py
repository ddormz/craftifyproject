# Generated by Django 4.2.7 on 2024-07-16 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_unidadmedidas'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='unidad_medida',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.unidadmedidas'),
        ),
    ]