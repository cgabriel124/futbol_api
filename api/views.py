from django.http import JsonResponse
from .models import *
from rest_framework import generics
from .serializers import *
from random import shuffle
# from django.db.models import Count


class EquipoCreateView(generics.CreateAPIView):
    # Aqui se crea el equipo
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class EquipoListView(generics.ListAPIView):
    # Aqui se listan todos los equipos
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class EquipoDetailView(generics.RetrieveAPIView):
    # Aqui se obtiene un cliente por su id
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


# Usar a modo de prueba, en general no se usa
class EquipoUpdateView(generics.RetrieveAPIView):
    # Aqui se actualiza un cliente por su id
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


# Usar a modo de prueba, en general no se usa
class EquipoDeleteView(generics.RetrieveAPIView):
    # Aqui se elimina un cliente por su id
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class JugadorCreateView(generics.CreateAPIView):
    # Aqui se crea el jugador
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer


class JugadorListView(generics.ListAPIView):
    # Aqui se listan todos los jugadores
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer


def team_distribution(request):
    # Obtener todos los jugadores y equipos
    jugadores = list(Jugador.objects.all())
    equipos = list(Equipo.objects.all())

    # Barajar aleatoriamente la lista de jugadores
    shuffle(jugadores)

    # Calcular el número de jugadores por equipo deseado (redondeando hacia arriba)
    jugadores_por_equipo = -(-len(jugadores) // len(equipos))

    # Iterar sobre los equipos y asignar jugadores
    for equipo in equipos:
        # Tomar los próximos jugadores en la lista
        jugadores_equipo = jugadores[:jugadores_por_equipo]

        # Actualizar la referencia del equipo para los jugadores
        for jugador in jugadores_equipo:
            jugador.id_equipo = equipo
            jugador.save()

        # Eliminar los jugadores asignados de la lista
        jugadores = jugadores[jugadores_por_equipo:]

    # Puedes ajustar el retorno según tus necesidades
    return JsonResponse({'message': 'ok'}, status=200)

