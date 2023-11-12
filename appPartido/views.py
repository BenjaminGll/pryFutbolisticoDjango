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
        try:
            encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
            descripcionEncuentroLocal_obj = descripcion_encuentro.objects.get(equipo=encuentro_obj.equipo_local)
            descripcionEncuentroVisita_obj = descripcion_encuentro.objects.get(equipo=encuentro_obj.equipo_visita)
            
            alineacionLocal_objs = alineacion.objects.filter(descripcion_encuentro_id=descripcionEncuentroLocal_obj.descripcion_encuentro_id)
            alineacionVisita_objs = alineacion.objects.filter(descripcion_encuentro_id=descripcionEncuentroVisita_obj.descripcion_encuentro_id)
            
            # Obtener una lista de IDs de contrato
            contratoLocal_ids = [a.contrato_id_id for a in alineacionLocal_objs if a.contrato_id_id]
            contratoVisita_ids = [a.contrato_id_id for a in alineacionVisita_objs if a.contrato_id_id]

            # Filtrar contratos por IDs
            contratoLocal_objs = contrato.objects.filter(contrato_id__in=contratoLocal_ids)
            contratoVisita_objs = contrato.objects.filter(contrato_id__in=contratoVisita_ids)

            # Obtener personas a partir de los contratos
            personaLocal_objs = persona.objects.filter(persona_id__in=[c.persona_id for c in contratoLocal_objs])
            personaVisita_objs = persona.objects.filter(persona_id__in=[c.persona_id for c in contratoVisita_objs])

            data = {
                'alineacion1_id': [str(persona) for persona in personaLocal_objs],
                'alineacion2_id': [str(persona) for persona in personaVisita_objs],
            }

            return JsonResponse(data)
        except alineacion.DoesNotExist:
            return JsonResponse({"error": "No se encontró la alineación para el encuentro dado."}, status=404)
        except contrato.DoesNotExist:
            return JsonResponse({"error": "No se encontró un contrato para la alineación dada."}, status=404)
        except Exception as e:
            print(f"Excepción no manejada: {str(e)}")
            return JsonResponse({"error": "Error interno del servidor."}, status=500)


