from django.http import JsonResponse
from django.views import View
from .models import *
from appEquipo.models import *
from appContrato.models import *
from django.shortcuts import render

class ObtenerEncuentrosView(View):
    def get(self, request, *args, **kwargs):
        competicion_id = request.GET.get('competicion_id')
        encuentros = encuentro.objects.filter(competicion_id=competicion_id)
        data = {encuentro.encuentro_id: str(encuentro) for encuentro in encuentros}
        return JsonResponse(data)
    
class ObtenerAlineacionesView(View):
    def get(self, request, *args, **kwargs):
        encuentro_id = request.GET.get('encuentro_id')
        tipo_evento_id = request.GET.get('tipo_evento_id')
        try:
            encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)

            # Obtener todos los objetos que cumplen con la condición
            descripcionEncuentroLocal_objs = descripcion_encuentro.objects.filter(equipo=encuentro_obj.equipo_local)
            descripcionEncuentroVisita_objs = descripcion_encuentro.objects.filter(equipo=encuentro_obj.equipo_visita)

            # Obtener alineaciones asociadas a los objetos obtenidos
            alineacionLocal_objs = alineacion.objects.filter(descripcion_encuentro_id__in=descripcionEncuentroLocal_objs)
            alineacionVisita_objs = alineacion.objects.filter(descripcion_encuentro_id__in=descripcionEncuentroVisita_objs)
            
            if (tipo_evento_id=='3'):
                data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],}
            elif (tipo_evento_id=='37'):
                 data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],}
            else:
                data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
                }    
            
            

            return JsonResponse(data)
        except encuentro.DoesNotExist:
            return JsonResponse({"error": "No se encontró el encuentro dado."}, status=404)
        except descripcion_encuentro.DoesNotExist:
            return JsonResponse({"error": "No se encontró la descripción del encuentro para el equipo dado."}, status=404)
        except alineacion.DoesNotExist:
            return JsonResponse({"error": "No se encontró la alineación para el encuentro dado."}, status=404)
        except Exception as e:
            print(f"Excepción no manejada: {str(e)}")
            return JsonResponse({"error": "Error interno del servidor."}, status=500)
def mostrarEncuentros(request):
    encuentros = encuentro.objects.filter(estado_jugado='E')
    return render(request, 'listarEncuentros.html', {'encuentros': encuentros})


def asignarAlineacion(request, encuentro_id):
    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    contratoLocal = contrato.objects.filter(nuevo_club=equipoLocal.equipo_id)
    contratoVisita = contrato.objects.filter(nuevo_club=equipoVisita.equipo_id)

    return render(request, 'asignarAlineaciones.html', {'encuentro': encuentro_obj, 'equipoLocal': contratoLocal, 'equipoVisita': contratoVisita})
