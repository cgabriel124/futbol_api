from django.shortcuts import render
from .models import Equipo
from rest_framework import generics
from .serializers import EquipoSerializer


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

#Usar a modo de prueba, en general no se usa
class EquipoUpdateView(generics.RetrieveAPIView):
    # Aqui se actualiza un cliente por su id
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
#Usar a modo de prueba, en general no se usa
class EquipoDeleteView(generics.RetrieveAPIView):
    # Aqui se elimina un cliente por su id
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer