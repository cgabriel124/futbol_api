from rest_framework import serializers
from .models import Equipo, Jugador, Partido


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['id_jugador', 'nombre', 'apellido', 'ano_nacimiento', 'posicion', 'nacionalidad']


class JugadorFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'


class EquipoSerializer(serializers.ModelSerializer):
    jugadores = JugadorSerializer(many=True, read_only=True)
    numero_jugadores = serializers.IntegerField()

    # logo = serializers.ImageField()
    class Meta:
        model = Equipo
        # fields = ['nombre_equipo', 'direccion', 'logo', 'descripcion', 'numero_jugadores']
        fields = ['id_equipo', 'nombre_equipo', 'direccion', 'logo', 'descripcion', 'numero_jugadores', 'jugadores']
        """
    def create(self, validated_data):
        logo_file = validated_data.pop('logo')
        validated_data['logo'] = logo_file.read()
        equipo = Equipo.objects.create(**validated_data)
        return equipo
        """


class JugadorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'ano_nacimiento', 'posicion', 'nacionalidad']


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ['fecha_partido', 'hora_partido', 'numero_goles']
