# Generated by Django 5.1.6 on 2025-03-08 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('rol', models.CharField(choices=[('ADMIN', 'ADMIN'), ('PM', 'PM'), ('CONTABILIDAD', 'CONTABILIDAD')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rutine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routines', to='bases.user')),
            ],
        ),
    ]
