from django.urls import path
from .views import *

urlpatterns = [
    path('teamcreate/', EquipoCreateView.as_view(), name='create-equipo'),
    path('teamlist/', EquipoListView.as_view(), name='list-equipo'),
    path('teamplayerlist/', get_equipo_list, name='equipo-jugador-list'),
    path('teamupdate/<int:pk>/', EquipoUpdateView.as_view(), name='update-equipo'),
    path('teamdelete/<int:pk>/', EquipoDeleteView.as_view(), name='delete-equipo'),
    path('playercreate/', JugadorCreateView.as_view(), name='create-jugador'),
    path('playerlist/', JugadorListView.as_view(), name='list-jugador'),
    # endpoint para la distribucion de jugadores por equipo
    path('teamdistribution/', team_distribution, name='distribution-team'),
    path('generatematches/', generate_matches, name='matches-generate'),
    path('getmatches/',get_partidos_info, name='get-matches'),
    path('registerresult/',RegisterMatchResult.as_view(), name='register-result'),
    path('getteamstats/', get_equipo_stats, name='get-team-stats'),
]
