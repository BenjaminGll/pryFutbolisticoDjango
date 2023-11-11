from django.http import JsonResponse
from django.views import View
from .models import *
from appPartido.models import *
from appContrato.models import *

class ObteneraJugadoresView(View):
    def get(self, request, *args, **kwargs):
        de_id = request.GET.get('descripcionId')
        descripcion_encuentros = descripcion_encuentro.objects.get(descripcion_encuentro_id=de_id)
        equipos = equipo.objects.get(equipo_id=descripcion_encuentros.equipo)
        contratos = contrato.objects.get(ultimo_club=equipos.equipo_id)
    
        data = {str(contrato.pk): str(contrato.persona) for contrato in contratos}
        return JsonResponse(data)




