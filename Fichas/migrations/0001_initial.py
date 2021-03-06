# Generated by Django 3.2.7 on 2021-12-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id_diagnostico', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'diagnostico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'equipo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id_historia', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'historia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Imagenologia',
            fields=[
                ('id_imagen', models.AutoField(primary_key=True, serialize=False)),
                ('ruta', models.URLField(blank=True, null=True, verbose_name='Enlace a Imagen')),
            ],
            options={
                'db_table': 'imagenologia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id_modalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'modalidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Observaciones',
            fields=[
                ('id_observaciones', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'observaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('id_diagnostico', models.IntegerField(blank=True, null=True, verbose_name='id_diagnostico')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('rut', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_nacimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('edad', models.CharField(blank=True, max_length=100, null=True)),
                ('prevision', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('alta', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'paciente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id_tecnica', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tecnica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id_tratamiento', models.AutoField(primary_key=True, serialize=False)),
                ('energia', models.CharField(blank=True, max_length=100, null=True)),
                ('zona_irradiada', models.CharField(blank=True, max_length=100, null=True)),
                ('dosis', models.CharField(blank=True, max_length=100, null=True)),
                ('profundidad_calculo', models.CharField(blank=True, max_length=100, null=True)),
                ('interrupciones', models.CharField(blank=True, max_length=100, null=True)),
                ('localizacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_inicio', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_termino', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tratamiento',
                'managed': False,
            },
        ),
    ]
