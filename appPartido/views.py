from django.http import JsonResponse
from django.views import View
from .models import *
from appEquipo.models import equipo
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

        encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)

        # Obtener todos los objetos que cumplen con la condición
        descripcionEncuentroLocal_objs = descripcion_encuentro.objects.filter(equipo=encuentro_obj.equipo_local)
        descripcionEncuentroVisita_objs = descripcion_encuentro.objects.filter(equipo=encuentro_obj.equipo_visita)

        # Obtener alineaciones asociadas a los objetos obtenidos
        alineacionLocal_objs = alineacion.objects.filter(descripcion_encuentro_id__in=descripcionEncuentroLocal_objs)
        alineacionVisita_objs = alineacion.objects.filter(descripcion_encuentro_id__in=descripcionEncuentroVisita_objs)

        if tipo_evento_id == '3':
            data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
            }
        elif tipo_evento_id == '37':
            data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
            }
        else:
            data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
            }

        return JsonResponse(data)


def mostrarEncuentros(request):
    encuentros = encuentro.objects.filter(estado_jugado='E')
    return render(request, 'listarEncuentros.html', {'encuentros': encuentros})

def asignarAlineacion(request, encuentro_id):
    if request.method == 'POST':
        jugadores_local = request.POST.getlist('jugadores_local[]', [])
        jugadores_visita = request.POST.getlist('jugadores_visita[]', [])

        # Guardar jugadores del equipo local
        for jugador_id in jugadores_local[:11]:
            if jugador_id:
                try:
                    contrato_local = contrato.objects.get(contrato_id=jugador_id)
                    alineacion_local = alineacion(
                        descripcion_encuentro_id=encuentro_id,
                        contrato_id=contrato_local,
                        dorsal=contrato_local.dorsal,
                        posicion_jugador_id=1,
                        capitan=False,
                        estado=True
                    )
                    alineacion_local.save()
                    print(f"Guardada alineación para el jugador {contrato_local.persona.nombre} en el equipo local.")
                except contrato.DoesNotExist:
                    print(f"No se encontró contrato para el jugador con ID {jugador_id}")
                except ValueError:
                    print(f"El ID del jugador no es un número válido: {jugador_id}")

        # Guardar jugadores del equipo visitante
        for jugador_id in jugadores_visita[:11]:
            if jugador_id:
                try:
                    contrato_visita = contrato.objects.get(contrato_id=jugador_id)
                    alineacion_visita = alineacion(
                        descripcion_encuentro_id=encuentro_id,
                        contrato_id=contrato_visita,
                        dorsal=contrato_visita.dorsal,
                        posicion_jugador_id=1,
                        capitan=False,
                        estado=True
                    )
                    alineacion_visita.save()
                    print(f"Guardada alineación para el jugador {contrato_visita.persona.nombre} en el equipo visitante.")
                except contrato.DoesNotExist:
                    print(f"No se encontró contrato para el jugador con ID {jugador_id}")
                except ValueError:
                    print(f"El ID del jugador no es un número válido: {jugador_id}")

    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    contratoLocal = contrato.objects.filter(nuevo_club=equipoLocal.equipo_id)
    contratoVisita = contrato.objects.filter(nuevo_club=equipoVisita.equipo_id)

    return render(request, 'asignarAlineaciones.html', {'encuentro': encuentro_obj, 'equipoLocal': contratoLocal, 'equipoVisita': contratoVisita})