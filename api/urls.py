from django.urls import include, path
from .views import EquipoCreateView, EquipoListView, EquipoDetailView, EquipoUpdateView, EquipoDeleteView

urlpatterns = [
    path('teamcreate/', EquipoCreateView.as_view(), name='create-equipo'),
    path('teamlist/', EquipoListView.as_view(), name='list-equipo'),
    path('teamdetail/<int:pk>/', EquipoDetailView.as_view(), name='detail-equipo'),
    path('teamupdate/<int:pk>/', EquipoUpdateView.as_view(), name='update-equipo'),
    path('teamdelete/<int:pk>/', EquipoDeleteView.as_view(), name='delete-equipo'),
]