# Generated by Django 4.2.5 on 2023-11-04 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_tareas_remove_avances_asignacion_asignacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusTarea',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_status', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Status de Tarea',
                'verbose_name_plural': 'Status de Tareas',
                'ordering': ['nombre_status'],
            },
        ),
        migrations.AddField(
            model_name='tareas',
            name='trabajador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas',
            name='status_tarea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.statustarea'),
        ),
    ]
