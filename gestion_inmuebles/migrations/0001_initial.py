# Generated by Django 5.1.3 on 2024-11-18 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m2_construidos', models.FloatField()),
                ('m2_totales', models.FloatField()),
                ('estacionamientos', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('banos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmuebles.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio_mensual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('caracteristicas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmuebles.caracteristicas')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmuebles.direccion')),
                ('tipo_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmuebles.tipoinmueble')),
            ],
        ),
    ]
