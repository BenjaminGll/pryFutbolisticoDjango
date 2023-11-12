from django.http import JsonResponse
from django.views import View
from .models import *
from appEquipo.models import *
from appContrato.models import *

class ObtenerEncuentrosView(View):
    def get(self, request, *args, **kwargs):
        competicion_id = request.GET.get('competicion_id')
        encuentros = encuentro.objects.filter(competicion_id=competicion_id)
        data = {encuentro.encuentro_id: str(encuentro) for encuentro in encuentros}
        return JsonResponse(data)
    
class ObtenerAlineacionesView(View):
    def get(self, request, *args, **kwargs):
        encuentro_id = request.GET.get('encuentro_id')
        encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
        descripcionEncuentroLocal_obj = descripcion_encuentro.objects.get(equipo=encuentro_obj.equipo_local)
        descripcionEncuentroVisita_obj = descripcion_encuentro.objects.get(equipo=encuentro_obj.equipo_visita)
        alineacionLocal_obj = alineacion.objects.get(descripcion_encuentro_id=descripcionEncuentroLocal_obj.descripcion_encuentro_id)
        alineacionVisita_obj = alineacion.objects.get(descripcion_encuentro_id=descripcionEncuentroVisita_obj.descripcion_encuentro_id)
        contratoLocal_obj = contrato.objects.get(contrato_id=alineacionLocal_obj.contrato_id)
        contratoVisita_obj = contrato.objects.get(contrato_id=alineacionVisita_obj.contrato_id)
        personaLocal_obj = persona.objects.get(persona_id=contratoLocal_obj.persona)
        personaVisita_obj = persona.objects.get(persona_id=contratoVisita_obj.persona)



        data = {
            'alineacion_local': [str(p) for p in personaLocal_obj],
            'alineacion_visita': [str(p) for p in personaVisita_obj],
        }
        return JsonResponse(data)

