from django.http import JsonResponse
from django.views import View
from .models import *
from appEquipo.models import equipo
from appContrato.models import *
from django.shortcuts import render
from django.contrib import messages

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
    try:
        if request.method == 'POST':
            print(request.POST)
            jugadores_local = request.POST.getlist('jugadores_local[]', [])
            jugadores_visita = request.POST.getlist('jugadores_visita[]', [])

            
            # Guardar jugadores del equipo local
            for jugador_id in jugadores_local[:11]:
                print(f"Processing local player with ID: {jugador_id}")
                if jugador_id:
                    contrato_local = contrato.objects.get(contrato_id=jugador_id)
                    descripcion_encuentro_local=descripcion_encuentro.objects.get(encuentro_id=encuentro_id)
                    posicionLocal=posicion_jugador.objects.get(posicion_jugador_id=contrato_local.posicion_jugador)
                    alineacion_local = alineacion(
                        descripcion_encuentro_id=descripcion_encuentro_local.descripcion_encuentro_id,
                        contrato_id=contrato_local,
                        dorsal=contrato_local.dorsal,  # Ajusta esto según tu modelo de datos
                        posicion_jugador_id=posicionLocal.posicion_jugador_id,  # Ajusta esto según tu modelo de datos
                        capitan=False,  # Ajusta esto según tus necesidades
                        estado=True  # Ajusta esto según tus necesidades
                    )
                    alineacion_local.save()

            # Guardar jugadores del equipo visitante
            for jugador_id in jugadores_visita[:11]:
                if jugador_id:
                    contrato_visita = contrato.objects.get(contrato_id=jugador_id)
                    descripcion_encuentro_visita=descripcion_encuentro.objects.get(encuentro_id=encuentro_id)
                    posicionVisita=posicion_jugador.objects.get(posicion_jugador_id=contrato_visita.posicion_jugador)
                    alineacion_visita = alineacion(
                        descripcion_encuentro_id=descripcion_encuentro_visita.descripcion_encuentro_id,
                        contrato_id=contrato_visita,
                        dorsal=contrato_visita.dorsal,  # Ajusta esto según tu modelo de datos
                        posicion_jugador_id=posicionVisita.posicion_jugador_id,  # Ajusta esto según tu modelo de datos
                        capitan=False,  # Ajusta esto según tus necesidades
                        estado=True  # Ajusta esto según tus necesidades
                    )
                    alineacion_visita.save()

        messages.success(request, 'Alineaciones guardadas correctamente.')

    except contrato.DoesNotExist as e:
        messages.error(request, f'Error al obtener contrato: {str(e)}')
    except ValueError as e:
        messages.error(request, f'Error de valor: {str(e)}')
    except Exception as e:
        messages.error(request, f'Error interno del servidor: {str(e)}')

    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    contratoLocal = contrato.objects.filter(nuevo_club=equipoLocal.equipo_id)
    contratoVisita = contrato.objects.filter(nuevo_club=equipoVisita.equipo_id)

    return render(request, 'asignarAlineaciones.html', {'encuentro': encuentro_obj, 'equipoLocal': contratoLocal, 'equipoVisita': contratoVisita})