from django.http import JsonResponse
from django.views import View
from .models import *
from appEquipo.models import equipo
from appContrato.models import *
from django.shortcuts import render,  redirect
from django.contrib import messages
from datetime import datetime

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

    tipo = request.GET.get('tipo', 'alineaciones')  

    # Obtén los encuentros según el tipo
    if tipo == 'alineaciones':
            encuentros = encuentro.objects.filter(estado_jugado='N')
    elif tipo == 'terna_arbitral':
            encuentros = encuentro.objects.filter(estado_jugado='N')
    elif tipo == 'eventos':
         encuentros = encuentro.objects.filter(estado_jugado='E')
    else:
          encuentros = encuentro.objects.all()

    return render(request, 'listarEncuentros.html', {'encuentros': encuentros, 'tipo': tipo})



def asignar(request, tipo, encuentro_id):
    if tipo == 'alineaciones':
        return render(request, 'asignarAlineaciones.html', {'encuentro_id': encuentro_id})
    elif tipo == 'terna_arbitral':
        return render(request, 'asignar_terna_arbitral.html', {'encuentro_id': encuentro_id})
    elif tipo == 'eventos':
        return render(request, 'asignarEventos.html', {'encuentro_id': encuentro_id})
    else:
        # Manejo de error o redirección predeterminada
        return render(request, 'asignarAlineaciones.html', {'encuentro_id': encuentro_id})
    


def asignarAlineacion(request, encuentro_id):
    
    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    contratoLocal = contrato.objects.filter(nuevo_club=equipoLocal.equipo_id)
    contratoVisita = contrato.objects.filter(nuevo_club=equipoVisita.equipo_id)
    if request.method == 'POST':
        jugadores_local = request.POST.getlist('jugadores_local[]', [])
        jugadores_visita = request.POST.getlist('jugadores_visita[]', [])
        formacion_local = request.POST.get('formacion_local', '4-3-3')  # Valor predeterminado
        formacion_visita = request.POST.get('formacion_visita', '4-3-3')  # Valor predeterminado

        # Obtener descripciones de encuentro local y visita
        descripcion_encuentro_local = descripcion_encuentro.objects.filter(equipo=equipoLocal).first()
        descripcion_encuentro_visita = descripcion_encuentro.objects.filter(equipo=equipoVisita).first()

        # Guardar jugadores del equipo local
        for jugador_id_local in jugadores_local[:11]:
            if jugador_id_local:
                contrato_local = contrato.objects.filter(persona_id=jugador_id_local).first()
                posicionLocal = posicion_jugador.objects.get(posicion_jugador_id=contrato_local.posicion_jugador.posicion_jugador_id)
                alineacion_local = alineacion(
                    descripcion_encuentro_id=descripcion_encuentro_local,
                    contrato_id=contrato_local,
                    dorsal=contrato_local.dorsal,
                    posicion_jugador_id=posicionLocal,
                    capitan=False,
                    estado=True,
                    formacion=formacion_local
                )
                alineacion_local.save()

        # Guardar jugadores del equipo visitante
        for jugador_id_visita in jugadores_visita[:11]:
            if jugador_id_visita:
                contrato_visita = contrato.objects.filter(persona_id=jugador_id_visita).first()
                posicionVisita = posicion_jugador.objects.get(posicion_jugador_id=contrato_visita.posicion_jugador.posicion_jugador_id)
                alineacion_visita = alineacion(
                    descripcion_encuentro_id=descripcion_encuentro_visita,
                    contrato_id=contrato_visita,
                    dorsal=contrato_visita.dorsal,
                    posicion_jugador_id=posicionVisita,
                    capitan=False,
                    estado=True,
                    formacion=formacion_visita
                )
                alineacion_visita.save()

        messages.success(request, 'Alineaciones guardadas correctamente.')
        #return redirect('lista_encuentros_N')


    return render(request, 'asignarAlineaciones.html', {'encuentro': encuentro_obj, 'equipoLocal': contratoLocal, 'equipoVisita': contratoVisita})

def asignarEventos(request, encuentro_id):
    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    contratoLocal = contrato.objects.filter(nuevo_club=equipoLocal.equipo_id)
    contratoVisita = contrato.objects.filter(nuevo_club=equipoVisita.equipo_id)
    tipos_evento_relacionados = tipo_evento.objects.all()
    eventos_obj = []

    if request.method == 'POST':
        jugadores_local = request.POST.getlist('jugadores_local[]', [])
        jugadores_visita = request.POST.getlist('jugadores_visita[]', [])
        motivo = request.POST.get('motivo', '')
        cantidad = request.POST.get('cantidad', 0)
        tiempo_reglamentario = request.POST.get('tiempo_reglamentario', '')
        tiempo_extra = request.POST.get('tiempo_extra', '')
        # Validar y formatear los valores de tiempo
        try:
            tiempo_reglamentario = datetime.strptime(tiempo_reglamentario, '%H:%M:%S').time()
            tiempo_extra = datetime.strptime(tiempo_extra, '%H:%M:%S').time()
        except ValueError:
            # Manejar el error o mostrar un mensaje al usuario
            messages.error(request, 'Formato de tiempo inválido. Utiliza el formato HH:MM:SS.')
            return render(request, 'asignarEventos.html', {'encuentro': encuentro_obj, 'equipoLocal': contratoLocal, 'equipoVisita': contratoVisita, 'tipos_evento_relacionados': tipos_evento_relacionados})

        estado_evento = True  # Puedes ajustar este valor según tus necesidades

        # Obtener descripciones de encuentro local y visita
        descripcion_encuentro_local = descripcion_encuentro.objects.filter(equipo=equipoLocal).first()
        descripcion_encuentro_visita = descripcion_encuentro.objects.filter(equipo=equipoVisita).first()

        # Guardar eventos del equipo local
        guardar_eventos(jugadores_local[:11], descripcion_encuentro_local, motivo, cantidad, tiempo_reglamentario, tiempo_extra, estado_evento)

        # Guardar eventos del equipo visitante
        guardar_eventos(jugadores_visita[:11], descripcion_encuentro_visita, motivo, cantidad, tiempo_reglamentario, tiempo_extra, estado_evento)

        eventos_obj = evento.objects.filter(encuentro_id=encuentro_obj)
        print(eventos_obj)
        messages.success(request, 'Eventos guardados correctamente.')

    return render(request, 'asignarEventos.html', {'encuentro': encuentro_obj, 'equipoLocal': contratoLocal, 'equipoVisita': contratoVisita, 'tipos_evento_relacionados': tipos_evento_relacionados, 'eventos_obj': eventos_obj})

def guardar_eventos(jugadores, descripcion_encuentro, motivo, cantidad, tiempo_reglamentario, tiempo_extra, estado_evento):
    for jugador_id in jugadores:
        if jugador_id:
            contrato_jugador = contrato.objects.get(persona_id=jugador_id)
            alineacion_jugador = alineacion.objects.get(contrato_id=contrato_jugador)  # Utilizar el campo correcto

            tipo_evento_seleccionado = tipo_evento.objects.first()  # Ajusta este valor según tus necesidades
            encuentro_obj = descripcion_encuentro.encuentro

            evento_obj = evento(
                tipo_evento_id=tipo_evento_seleccionado,
                competicion_id=None,
                encuentro_id=encuentro_obj,
                alineacion1_id=alineacion_jugador,
                alineacion2_id=alineacion_jugador,  # Ajusta este valor según tus necesidades
                tiempo_reglamentario=tiempo_reglamentario,
                tiempo_extra=tiempo_extra,
                motivo=motivo,
                cantidad=cantidad,
                estado_evento=estado_evento
            )
            evento_obj.save()