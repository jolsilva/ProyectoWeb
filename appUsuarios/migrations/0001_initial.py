# Generated by Django 3.1.3 on 2020-11-18 18:06

import appUsuarios.rutificador
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club_Lectores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroTarjeta', models.TextField(max_length=10)),
                ('saldoDisponible', models.IntegerField()),
                ('rut', models.TextField(max_length=12, validators=[appUsuarios.rutificador.validate_rutificador])),
                ('clave', models.TextField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20)),
                ('apellidos', models.TextField(max_length=20)),
                ('rut', models.TextField(max_length=12, validators=[appUsuarios.rutificador.validate_rutificador])),
                ('sexo', models.TextField(max_length=10)),
                ('email', models.TextField(max_length=20)),
                ('contacto', models.TextField(max_length=12)),
            ],
        ),
    ]
