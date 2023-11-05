# Generated by Django 4.2.5 on 2023-11-04 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_equipos_observaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleEquipo',
            fields=[
                ('id_Detalle', models.AutoField(primary_key=True, serialize=False)),
                ('equipo_id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipos')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Material de Equipo',
                'verbose_name_plural': 'Materiales de Equipos',
                'ordering': ['equipo_id_equipo'],
            },
        ),
    ]
