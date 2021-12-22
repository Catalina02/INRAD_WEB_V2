from django.db import models


class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)#
    class Meta:
        managed = False
        db_table = 'diagnostico'


#Maquina con la cual se Trata al paciente
class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)#
    descripcion = models.TextField(blank=True, null=True)# 

    class Meta:
        managed = False
        db_table = 'equipo'

# Historial Medico de paciente 
class Historia(models.Model):
    id_historia = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)#

    class Meta:
        managed = False
        db_table = 'historia'

#link a la imagen
class Imagenologia(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    ruta = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenologia'


class Modalidad(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'


class Observaciones(models.Model):
    id_observaciones = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observaciones'


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_tratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='id_tratamiento')
    id_diagnostico = models.ForeignKey(Diagnostico, models.DO_NOTHING, db_column='id_diagnostico')
    id_historia = models.ForeignKey(Historia, models.DO_NOTHING, db_column='id_historia')
    id_observaciones = models.ForeignKey(Observaciones, models.DO_NOTHING, db_column='id_observaciones')
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    rut = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    edad = models.CharField(max_length=100, blank=True, null=True)
    prevision = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    numero_telefono = models.CharField(max_length=100, blank=True, null=True)
    alta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class Tecnica(models.Model):
    id_tecnica = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnica'


class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    id_modalidad = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='id_modalidad')
    id_equipo = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='id_equipo')
    id_tecnica = models.ForeignKey(Tecnica, models.DO_NOTHING, db_column='id_tecnica')
    energia = models.CharField(max_length=100, blank=True, null=True)
    zona_irradiada = models.CharField(max_length=100, blank=True, null=True)
    dosis = models.CharField(max_length=100, blank=True, null=True)
    profundidad_calculo = models.CharField(max_length=100, blank=True, null=True)
    interrupciones = models.CharField(max_length=100, blank=True, null=True)
    localizacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.CharField(max_length=100, blank=True, null=True)
    fecha_termino = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento'