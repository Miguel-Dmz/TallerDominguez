# Generated by Django 5.1.1 on 2024-10-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apaterno', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('Amaterno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre (s)')),
                ('Fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('Fecha_ingreso', models.DateField(verbose_name='Fecha ingreso')),
            ],
        ),
    ]
