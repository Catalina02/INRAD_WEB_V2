from django.db import models
from django.db.models.deletion import CASCADE

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_tratamiento = models.IntegerField(blank=True, null=True)
    id_diagnostico = models.IntegerField(blank=True, null=True)
    id_historia = models.IntegerField(blank=True, null=True)
    id_observaciones = models.IntegerField(blank=True, null=True)
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
    def __str__(self):
        return str(self.nombre)+' '+str(self.apellido)
class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)#
    paciente=models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_id')
    class Meta:
        managed = False
        db_table = 'diagnostico'
    def __str__(self):
        return ''
class Historia(models.Model):
    id_historia = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)#
    paciente=models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_id')
    class Meta:
        managed = False
        db_table = 'historia'
    def __str__(self):
        return ''
class Observaciones(models.Model):
    id_observaciones = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    paciente=models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_id')
    class Meta:
        managed = False
        db_table = 'observaciones'
    def __str__(self):
        return ''
#link a la imagen
class Imagenologia(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    ruta = models.URLField(null=True,blank=True,verbose_name="Enlace a Imagen")

    class Meta:
        managed = False
        db_table = 'imagenologia'
    def __str__(self):
        return ''

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)#
    descripcion = models.TextField(blank=True, null=True)# 
    

    class Meta:
        managed = False
        db_table = 'equipo'

class Modalidad(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'

class Tecnica(models.Model):
    id_tecnica = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnica'


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)#
    descripcion = models.TextField(blank=True, null=True)# 
    

    class Meta:
        managed = False
        db_table = 'equipo'
    def __str__(self):
        return str(self.nombre)

class Modalidad(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'
    def __str__(self):
        return str(self.nombre)

class Tecnica(models.Model):
    id_tecnica = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnica'
    def __str__(self):
        return str(self.nombre)


class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    modalidad = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='modalidad_id')
    equipo = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='equipo_id')
    tecnica = models.ForeignKey(Tecnica, models.DO_NOTHING, db_column='tecnica_id')
    energia = models.CharField(max_length=100, blank=True, null=True)
    zona_irradiada = models.CharField(max_length=100, blank=True, null=True)
    dosis = models.CharField(max_length=100, blank=True, null=True)
    profundidad_calculo = models.CharField(max_length=100, blank=True, null=True)
    interrupciones = models.CharField(max_length=100, blank=True, null=True)
    localizacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.CharField(max_length=100, blank=True, null=True)
    fecha_termino = models.CharField(max_length=100, blank=True, null=True)
    paciente=models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_id')
    class Meta:
        managed = False
        db_table = 'tratamiento'
    def __str__(self):
        return 'Tratamiento Paciente: '+str(self.paciente.nombre)+' '+str(self.paciente.apellido)