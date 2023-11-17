from rest_framework import serializers
from .models import Equipo, Jugador, Partido, Equipo_Partido


class EquipoSerializer(serializers.ModelSerializer):
    #logo = serializers.ImageField()
    class Meta:
        model = Equipo
        #fields = ['nombre_equipo', 'direccion', 'logo', 'descripcion', 'numero_jugadores']
        fields = ['nombre_equipo', 'direccion', 'descripcion', 'numero_jugadores']
        """
    def create(self, validated_data):
        logo_file = validated_data.pop('logo')
        validated_data['logo'] = logo_file.read()
        equipo = Equipo.objects.create(**validated_data)
        return equipo
        """
class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'ano_nacimiento', 'posicion', 'nacionalidad']

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ['fecha_partido', 'hora_partido', 'numero_goles']

class Equipo_PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo_Partido
        fields = ['id_equipo', 'id_partido', 'resultado', 'goles_ganador', 'goles_perdedor']