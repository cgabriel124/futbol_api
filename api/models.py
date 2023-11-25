from django.db import models


# Create your models here.

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    ###logo = models.BinaryField(null=True, blank=True)
    descripcion = models.CharField(max_length=300)
    numero_jugadores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre_equipo


class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ano_nacimiento = models.IntegerField()
    posicion = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    equipo_local = models.ForeignKey(Equipo, related_name='partidos_local', on_delete=models.CASCADE, null=True, blank=True)
    equipo_visitante = models.ForeignKey(Equipo, related_name='partidos_visitante', on_delete=models.CASCADE, null=True, blank=True)
    equipo_ganador = models.ForeignKey('Equipo', related_name='partidos_ganados', null=True, blank=True, on_delete=models.CASCADE)
    goles_local = models.PositiveIntegerField()
    goles_visitante = models.PositiveIntegerField()
    fecha_partido = models.DateField()
    hora_partido = models.TimeField()
    def __str__(self):
        return self.id_partido

'''
class Equipo_Partido(models.Model):
    id_equipo_partido = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    resultado = models.IntegerField()
    goles_ganador = models.IntegerField()
    goles_perdedor = models.IntegerField()

    def __str__(self):
        return self.id_equipo_partido
'''