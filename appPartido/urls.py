from django.urls import path
from .views import ObtenerEncuentrosView, ObtenerAlineacionesView

urlpatterns = [
    path('get_encuentros/', ObtenerEncuentrosView.as_view(), name='get_encuentros'),
    path('get_alineaciones/', ObtenerAlineacionesView.as_view(), name='get_alineaciones'),

]
