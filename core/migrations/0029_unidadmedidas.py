# Generated by Django 4.2.7 on 2024-07-16 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_proyecto_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadMedidas',
            fields=[
                ('id_unidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_unidad', models.CharField(max_length=10)),
            ],
        ),
    ]