from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import JsonResponse
from django.views import View
from rest_framework.generics import ListAPIView
from .models import *
from rest_framework import generics
from .serializers import *
from random import shuffle
#from django.db.models import F, Q, Count, Case, When, IntegerField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class EquipoCreateView(generics.CreateAPIView):
    # Aqui se crea el equipo
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    def perform_create(self, serializer):
        # Procesar la imagen si se proporciona en la solicitud
        logo_file = self.request.FILES.get('logo')
        if logo_file:
            # Puedes querer cambiar el nombre del archivo para evitar conflictos
            serializer.validated_data['logo'] = SimpleUploadedFile(logo_file.name, logo_file.read())

        # Llamar al método perform_create del padre para guardar el objeto Equipo
        super().perform_create(serializer)


class EquipoListView(ListAPIView):
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
    serializer_class = JugadorFullSerializer


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
    print("Distribucion de jugadores exitosa")
    # Puedes ajustar el retorno según tus necesidades
    return JsonResponse({'message': 'ok'}, status=200)


# test############# Borrar

@api_view(['GET'])
def get_equipo_list(request):
    equipos = Equipo.objects.all()

    data = []
    for equipo in equipos:
        jugadores_equipo = Jugador.objects.filter(id_equipo=equipo.id_equipo)
        jugadores_data = JugadorSerializer(jugadores_equipo, many=True).data

        equipo_data = {
            'id_equipo': equipo.id_equipo,
            'nombre_equipo': equipo.nombre_equipo,
            'direccion': equipo.direccion,
            'descripcion': equipo.descripcion,
            'numero_jugadores': len(jugadores_data),
            'jugadores': jugadores_data
        }

        data.append(equipo_data)
    return JsonResponse({'team_data': data}, status=200)


def generate_matches(request):
    # Obtener todos los equipos
    equipos = list(Equipo.objects.all())

    # Barajar aleatoriamente la lista de equipos
    shuffle(equipos)

    # Iterar sobre los equipos y crear partidos
    for i in range(len(equipos)):
        equipo_local = equipos[i]

        for j in range(i + 1, len(equipos)):
            equipo_visitante = equipos[j]

            # Crear un partido con equipos y valores iniciales
            partido = Partido.objects.create(
                equipo_local=equipo_local,
                equipo_visitante=equipo_visitante,
                goles_local=0,
                goles_visitante=0,
                fecha_partido=datetime.now() + timedelta(days=i),
                hora_partido=datetime.strptime("13:00", "%H:%M").time()
            )

            # Puedes imprimir o hacer otras operaciones con el partido si es necesario
            # print(f"Partido creado: {partido}")

    print("Creación de partidos exitosa")
    # Puedes ajustar el retorno según tus necesidades
    return JsonResponse({'message': 'ok'}, status=200)


def get_partidos_info(request):
    # Obtener todos los partidos
    partidos = Partido.objects.all()

    # Crear una lista para almacenar la información de cada partido
    partidos_info = []

    # Iterar sobre los partidos y extraer la información necesaria
    for partido in partidos:
        partido_info = {
            'id_partido': partido.id_partido,
            'id_equipo_local': partido.equipo_local.id_equipo,
            'nombre_equipo_local': partido.equipo_local.nombre_equipo,
            'id_equipo_visitante': partido.equipo_visitante.id_equipo,
            'nombre_equipo_visitante': partido.equipo_visitante.nombre_equipo,
        }

        # Agregar la información del partido a la lista
        partidos_info.append(partido_info)

    # Puedes ajustar el retorno según tus necesidades
    return JsonResponse({'partidos_info': partidos_info}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class RegisterMatchResult(View):
    def post(self, request, *args, **kwargs):
        try:
            # Obtener datos del cuerpo del request
            data = json.loads(request.body.decode('utf-8'))

            # Obtener información del partido desde el cuerpo del request
            id_partido = data['id_partido']
            id_equipo_local = data['id_equipo_local']
            id_equipo_visitante = data['id_equipo_visitante']
            goles_local = data['goles_local']
            goles_visitante = data['goles_visitante']

            # Obtener el partido a través del ID
            partido = Partido.objects.get(id_partido=id_partido)

            # Actualizar la información del partido
            partido.equipo_local_id = id_equipo_local
            partido.equipo_visitante_id = id_equipo_visitante
            partido.goles_local = goles_local
            partido.goles_visitante = goles_visitante

            if goles_local > goles_visitante:
                partido.equipo_ganador = partido.equipo_local
            elif goles_local < goles_visitante:
                partido.equipo_ganador = partido.equipo_visitante
            else:
                # Empate, no hay un ganador
                partido.equipo_ganador = None

            partido.save()
            # Guardar los cambios en el modelo
            partido.save()

            # Puedes ajustar el retorno según tus necesidades
            return JsonResponse({'message': 'Resultado del partido registrado exitosamente'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


def get_equipo_stats(request):
    # Obtener todos los partidos
    partidos = Partido.objects.all()

    # Crear un diccionario para almacenar la información de cada equipo
    equipos_info = {}

    # Iterar sobre los partidos y calcular los resultados para cada equipo
    for partido in partidos:
        # Calcular el resultado del partido
        if partido.goles_local > partido.goles_visitante:
            resultado = 'ganado_local'
            equipo_ganador_id = partido.equipo_local.id_equipo
            equipo_perdedor_id = partido.equipo_visitante.id_equipo
        elif partido.goles_local < partido.goles_visitante:
            resultado = 'ganado_visitante'
            equipo_ganador_id = partido.equipo_visitante.id_equipo
            equipo_perdedor_id = partido.equipo_local.id_equipo
        else:
            resultado = 'empate'
            equipo_ganador_id = None
            equipo_perdedor_id = None

        # Actualizar la información del equipo ganador
        if equipo_ganador_id is not None:
            if equipo_ganador_id in equipos_info:
                equipos_info[equipo_ganador_id]['ganados'] += 1
            else:
                equipos_info[equipo_ganador_id] = {'ganados': 1, 'empatados': 0, 'perdidos': 0}

        # Actualizar la información del equipo perdedor
        if equipo_perdedor_id is not None:
            if equipo_perdedor_id in equipos_info:
                equipos_info[equipo_perdedor_id]['perdidos'] += 1
            else:
                equipos_info[equipo_perdedor_id] = {'ganados': 0, 'empatados': 0, 'perdidos': 1}

        # Actualizar la información en caso de empate
        if resultado == 'empate':
            if partido.equipo_local.id_equipo in equipos_info:
                equipos_info[partido.equipo_local.id_equipo]['empatados'] += 1
            else:
                equipos_info[partido.equipo_local.id_equipo] = {'ganados': 0, 'empatados': 1, 'perdidos': 0}

            if partido.equipo_visitante.id_equipo in equipos_info:
                equipos_info[partido.equipo_visitante.id_equipo]['empatados'] += 1
            else:
                equipos_info[partido.equipo_visitante.id_equipo] = {'ganados': 0, 'empatados': 1, 'perdidos': 0}

    # Crear una lista para almacenar la información de cada equipo
    equipos_info_list = []

    # Iterar sobre el diccionario de información de equipos y agregar a la lista
    for equipo_id, info in equipos_info.items():
        equipo_info = {
            'id_equipo': equipo_id,
            'nombre_equipo': Equipo.objects.get(id_equipo=equipo_id).nombre_equipo,
            'ganados': info['ganados'],
            'empatados': info['empatados'],
            'perdidos': info['perdidos'],
        }
        equipos_info_list.append(equipo_info)

    # Puedes ajustar el retorno según tus necesidades
    return JsonResponse({'equipos_info': equipos_info_list}, status=200)


