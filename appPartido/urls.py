from django.urls import path    
from .views import *

urlpatterns = [
    path('get_encuentros/', ObtenerEncuentrosView.as_view(), name='get_encuentros'),
    path('get_alineaciones/', ObtenerAlineacionesView.as_view(), name='get_alineaciones'),
    path('lista_encuentros_E/', mostrarEncuentrosEnJuego, name='lista_encuentros_E'),
    path('lista_encuentros_N/', mostrarEncuentrosNoJugado, name='lista_encuentros_N'),
    path('asignarAlineaciones/<int:encuentro_id>/', asignarAlineacion, name='asignarAlineaciones'),




]
