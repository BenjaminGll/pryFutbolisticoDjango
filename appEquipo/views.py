from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import *
from appPartido.models import *
from appContrato.models import *

class ObteneraJugadoresView(View):
    def get(self, request, *args, **kwargs):
        de_id = request.GET.get('descripcion_encuentro_id')

        try:
            descripcion_encuentro_obj = descripcion_encuentro.objects.get(descripcion_encuentro_id=de_id)
            equipos = equipo.objects.get(equipo_id=descripcion_encuentro_obj.equipo)
            contratos = contrato.objects.filter(ultimo_club=equipos.equipo_id)
        
            data = {str(contrato.pk): str(contrato.persona) for contrato in contratos}
            return JsonResponse(data)
        
        except ObjectDoesNotExist:
            return JsonResponse({"error": "El objeto no existe."}, status=404)
        
        except MultipleObjectsReturned:
            return JsonResponse({"error": "Múltiples objetos encontrados. Revisa tus datos."}, status=500)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
