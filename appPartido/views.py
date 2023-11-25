from django.http import JsonResponse
from django.views import View
from .models import *
from appCompeticion.models import *
from appEquipo.models import *
from appContrato.models import *
from django.shortcuts import render, get_object_or_404,  redirect
from django.contrib import messages
from datetime import datetime


class ObtenerEncuentrosView(View):
    def get(self, request, *args, **kwargs):
        competicion_id = request.GET.get('competicion_id')
        encuentros = encuentro.objects.filter(competicion_id=competicion_id)
        data = {encuentro.encuentro_id: str(
            encuentro) for encuentro in encuentros}
        return JsonResponse(data)


class ObtenerAlineacionesView(View):
    def get(self, request, *args, **kwargs):
        encuentro_id = request.GET.get('encuentro_id')
        tipo_evento_id = request.GET.get('tipo_evento_id')

        encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)

        # Obtener todos los objetos que cumplen con la condición
        descripcionEncuentroLocal_objs = descripcion_encuentro.objects.filter(
            equipo=encuentro_obj.equipo_local)
        descripcionEncuentroVisita_objs = descripcion_encuentro.objects.filter(
            equipo=encuentro_obj.equipo_visita)

        # Obtener alineaciones asociadas a los objetos obtenidos
        alineacionLocal_objs = alineacion.objects.filter(
            descripcion_encuentro_id__in=descripcionEncuentroLocal_objs)
        alineacionVisita_objs = alineacion.objects.filter(
            descripcion_encuentro_id__in=descripcionEncuentroVisita_objs)

        if tipo_evento_id == '3':
            data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
            }
        elif tipo_evento_id == '37':
            data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
            }
        else:
            data = {
                'alineacion1': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionLocal_objs],
                'alineacion2': [{'id': str(alineacion.alineacion_id), 'jugador': str(alineacion.contrato_id)} for alineacion in alineacionVisita_objs],
            }

        return JsonResponse(data)

def mostrarEncuentros(request):
    tipo = request.GET.get('tipo', 'Alineacion')

    if request.method == 'POST':
        competicion_id = request.POST.get('competicion')
        fase_id = request.POST.get('fase')
        grupo_id = request.POST.get('grupo')
        return redirect('lista_encuentros')

    # Obtén los encuentros según el tipo
    if tipo == 'alineaciones':
        encuentros = encuentro.objects.filter(estado_jugado='N')
    elif tipo == 'terna_arbitral':
        encuentros = encuentro.objects.filter(estado_jugado='N')
    elif tipo == 'eventos':
        encuentros = encuentro.objects.filter(estado_jugado='E')
    elif tipo == 'estadisticas':
        encuentros = encuentro.objects.filter(estado_jugado='E')
    else:
        encuentros = encuentro.objects.all()

    # Aplica filtros adicionales si se proporcionan
    if 'competicion_id' in locals():
        encuentros = encuentros.filter(competicion_id=competicion_id)
    if 'fase_id' in locals():
        encuentros = encuentros.filter(fase_id=fase_id)
    if 'grupo_id' in locals():
        encuentros = encuentros.filter(grupo_id=grupo_id)

    # Obtén las opciones para los combobox de filtro
    competiciones = competicion.objects.all()
    fases = fase.objects.all()
    grupos = grupo.objects.all()

    # Obtén las opciones seleccionadas para los filtros
    selected_competicion = int(competicion_id) if 'competicion_id' in locals() else None
    selected_fase = int(fase_id) if 'fase_id' in locals() else None
    selected_grupo = int(grupo_id) if 'grupo_id' in locals() else None

    return render(
        request,
        'listarEncuentros.html',
        {
            'encuentros': encuentros,
            'tipo': tipo,
            'competiciones': competiciones,
            'fases': fases,
            'grupos': grupos,
            'selected_competicion': selected_competicion,
            'selected_fase': selected_fase,
            'selected_grupo': selected_grupo,
        }
    )


def asignar(request, tipo, encuentro_id):
    if tipo == 'alineaciones':
        return render(request, 'asignarAlineaciones.html', {'encuentro_id': encuentro_id})
    elif tipo == 'terna_arbitral':
        return render(request, 'asignar_terna_arbitral.html', {'encuentro_id': encuentro_id})
    elif tipo == 'eventos':
        return render(request, 'asignarEventos.html', {'encuentro_id': encuentro_id})
    elif tipo == 'estadisticas':
        return render(request, 'asignarEstadisticas.html', {'encuentro_id': encuentro_id})
    else:
        # Manejo de error o redirección predeterminada
        return render(request, 'asignarAlineaciones.html', {'encuentro_id': encuentro_id})



def asignarAlineacion(request, encuentro_id):
    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    contratoLocal = contrato.objects.filter(
        nuevo_club=equipoLocal.equipo_id).exclude(persona__tipo_persona_id=2)
    contratoVisita = contrato.objects.filter(
        nuevo_club=equipoVisita.equipo_id).exclude(persona__tipo_persona_id=2)
    # Verificar si ya hay alineaciones registradas para este encuentro
    alineaciones_local = alineacion.objects.filter(
        descripcion_encuentro_id__encuentro=encuentro_obj, descripcion_encuentro_id__equipo=equipoLocal, estado=True)
    alineaciones_visita = alineacion.objects.filter(
        descripcion_encuentro_id__encuentro=encuentro_obj, descripcion_encuentro_id__equipo=equipoVisita,estado=True)

    # Obtener los IDs de los jugadores en la alineación para este encuentro específico
    jugadores_en_alineacion_local = set(
        alineaciones_local.values_list('contrato_id__persona_id', flat=True))
    jugadores_en_alineacion_visita = set(
        alineaciones_visita.values_list('contrato_id__persona_id', flat=True))

    # Obtener formación actual de cada equipo
    formacion_local_actual = alineaciones_local.first(
    ).formacion if alineaciones_local.exists() else '4-3-3'
    formacion_visita_actual = alineaciones_visita.first(
    ).formacion if alineaciones_visita.exists() else '4-3-3'

    if request.method == 'POST':
        alineaciones_local.delete()
        alineaciones_visita.delete()
        jugadoresLocales=  request.POST.getlist('jugadoresLocales[]', [])
        jugadoresVisitas=  request.POST.getlist('jugadoresVisitas[]', [])
        jugadores_local_sel = request.POST.getlist('jugadores_local[]', [])
        jugadores_visita_sel = request.POST.getlist('jugadores_visita[]', [])
        formacion_local = request.POST.get('formacion_local', '4-3-3')
        formacion_visita = request.POST.get('formacion_visita', '4-3-3')

        capitan_local = request.POST.get('capitan_local', None)
        capitan_visita = request.POST.get('capitan_visita', None)
        # Validate that both teams have exactly 11 players
        if len(jugadores_local_sel) != 11 or len(jugadores_visita_sel) != 11:
            messages.success(
                request, 'Debe seleccionar exactamente 11 jugadores por equipo.')
            return redirect(f"/appPartido/asignar/alineaciones/{encuentro_id}/")

        # Obtener descripciones de encuentro local y visita
        descripcion_encuentro_local = descripcion_encuentro.objects.filter(
            equipo=equipoLocal, encuentro=encuentro_obj).first()
        descripcion_encuentro_visita = descripcion_encuentro.objects.filter(
            equipo=equipoVisita, encuentro=encuentro_obj).first()
        # Guardar jugadores del equipo local
        for jugador_id_local in jugadoresLocales[:40]:
            if jugador_id_local:
                contrato_local = contrato.objects.filter(
                    persona_id=jugador_id_local).first()
                posicionLocal = posicion_jugador.objects.get(
                    posicion_jugador_id=contrato_local.posicion_jugador.posicion_jugador_id)
                for i in jugadores_local_sel[:11]:
                    estadoJugadorLocal = (jugador_id_local == i)
                    if estadoJugadorLocal == False:
                        estadoJugadorLocal = False
                    else:
                        break
                # Verifica si este jugador es el capitán
                capitanL = (jugador_id_local == capitan_local)
                alineacion_local = alineacion(
                    descripcion_encuentro_id=descripcion_encuentro_local,
                    contrato_id=contrato_local,
                    dorsal=contrato_local.dorsal,
                    posicion_jugador_id=posicionLocal,
                    capitan=capitanL,  # Usa el valor booleano aquí
                    estado=estadoJugadorLocal,
                    formacion=formacion_local
                )
                alineacion_local.save()

        # Guardar jugadores del equipo visitante
        for jugador_id_visita in jugadoresVisitas[:40]:
                if jugador_id_visita:
                    contrato_visita = contrato.objects.filter(
                        persona_id=jugador_id_visita).first()
                    posicionVisita = posicion_jugador.objects.get(
                        posicion_jugador_id=contrato_visita.posicion_jugador.posicion_jugador_id)
                    for i in jugadores_visita_sel[:11]:
                        estadoJugadorVisita = (jugador_id_visita == i)
                        if estadoJugadorVisita == False:
                            estadoJugadorVisita = False
                        else:
                            break    
                        # Verifica si este jugador es el capitán
                    capitanV = (jugador_id_visita == capitan_visita)
                    alineacion_visita = alineacion(
                        descripcion_encuentro_id=descripcion_encuentro_visita,
                        contrato_id=contrato_visita,
                        dorsal=contrato_visita.dorsal,
                        posicion_jugador_id=posicionVisita,
                        capitan=capitanV,  # Usa el valor booleano aquí
                        estado=estadoJugadorVisita,
                        formacion=formacion_visita
                    )
                    alineacion_visita.save()

        messages.success(request, 'Alineaciones guardadas correctamente.')
        return redirect("/appPartido/lista_encuentros/?tipo=alineaciones")

    return render(request, 'asignarAlineaciones.html', {
        'encuentro': encuentro_obj,
        'equipoLocal': contratoLocal,
        'equipoVisita': contratoVisita,
        'jugadores_en_alineacion_local': jugadores_en_alineacion_local,
        'jugadores_en_alineacion_visita': jugadores_en_alineacion_visita,
        'formacion_local_actual': formacion_local_actual,
        'formacion_visita_actual': formacion_visita_actual,
    })


def asignarEventos(request, encuentro_id):
    tipos_evento_relacionados = tipo_evento.objects.all()
    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    alineacion01 = contrato.objects.filter(nuevo_club=equipoLocal.equipo_id)
    alineacion02 = contrato.objects.filter(nuevo_club=equipoVisita.equipo_id)

    evento_id = evento.objects.all()
    if request.method == 'POST':
        tipo_evento_id = request.POST.get('tipos_evento_relacionados', None)
        alineacion01 = request.POST.get('alineacion01', None)
        alineacion02 = request.POST.get('alineacion02', None)
        tiempo = request.POST.get('tiempo', 0)
        tiempo = int(tiempo) if tiempo else 0
        motivo = request.POST.get('motivo', '')
        encuentro_id = int(encuentro_id) if encuentro_id else 0

        print("Tipo de Evento ID:", tipo_evento_id)
        print("Alineación 01 List:", alineacion01)
        print("Alineación 02 List:", alineacion02)
        print("Tiempo:", tiempo)
        print("Motivo:", motivo)
        print("Encuentro:", encuentro_id)

        evento_obj = evento(
            tipo_evento_id=tipo_evento_id,
            contrato1_id=contrato.objects.get(contrato_id=alineacion01),
            contrato2_id=contrato.objects.get(contrato_id=alineacion02),
            encuentro_id=encuentro_obj,
            motivo=motivo,
            tiempo=tiempo
        )
        evento_obj.save()

        messages.success(request, 'Eventos guardados correctamente.')

    return render(request, 'asignarEventos.html', {
        'fecha_encuentro': encuentro_obj.fecha,
        'encuentro_id': encuentro_id,
        'equipoLocal': equipoLocal,
        'equipoVisita': equipoVisita,
        'evento_id': evento_id,
        'tipos_evento_relacionados': tipos_evento_relacionados,
        'alineacion01': alineacion01,
        'alineacion02': alineacion02,
    })


def asignarEstadisticas(request, encuentro_id):
    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    equipoLocal = equipo.objects.get(nombre=encuentro_obj.equipo_local)
    equipoVisita = equipo.objects.get(nombre=encuentro_obj.equipo_visita)
    descripcion_encuentro_local = descripcion_encuentro.objects.filter(equipo=equipoLocal).first()
    descripcion_encuentro_visita = descripcion_encuentro.objects.filter(equipo=equipoVisita).first()

    if request.method == 'POST':

        # Estadísticas Equipo Local
        posesion_balon_local = request.POST['posesion_balon_equipo1']
        pases_acertados_local = request.POST['pases_acertados_equipo1'] 
        tiros_desviados_local = request.POST['tiros_desviados_equipo1']
        efectividad_pases_local = request.POST['efectividad_pases_equipo1']
        tiros_indirectos_arco_local = request.POST['tiros_indirectos_arco_equipo1']
        tiros_directos_arco_local = request.POST['tiros_directos_arco_equipo1']

        # Estadísticas Equipo Visitante
        posesion_balon_visitante = request.POST['posesion_balon_equipo2'] 
        pases_acertados_visitante = request.POST['pases_acertados_equipo2']
        tiros_desviados_visitante = request.POST['tiros_desviados_equipo2'] 
        efectividad_pases_visitante = request.POST['efectividad_pases_equipo2']
        tiros_indirectos_arco_visitante = request.POST['tiros_indirectos_arco_equipo2']
        tiros_directos_arco_visitante = request.POST['tiros_directos_arco_equipo2']

        
        # Guardamos estadísticas local
        estadistica_local = estadisticas() 
        estadistica_local.posesion_balon = posesion_balon_local
        estadistica_local.pases_acertados = pases_acertados_local 
        estadistica_local.tiros_desviados = tiros_desviados_local
        estadistica_local.efectividad_pases = efectividad_pases_local
        estadistica_local.tiros_indirectos_arco = tiros_indirectos_arco_local
        estadistica_local.tiros_directos_arco = tiros_directos_arco_local 
        estadistica_local.descripcion_encuentro_id = desc_encuentro_local
        estadistica_local.save()
        
        # Guardamos estadísticas visitante
        estadistica_visitante = estadisticas()
        estadistica_visitante.posesion_balon = posesion_balon_visitante
        estadistica_visitante.pases_acertados = pases_acertados_visitante
        estadistica_visitante.tiros_desviados = tiros_desviados_visitante
        estadistica_visitante.efectividad_pases = efectividad_pases_visitante
        estadistica_visitante.tiros_indirectos_arco = tiros_indirectos_arco_visitante
        estadistica_visitante.tiros_directos_arco = tiros_directos_arco_visitante
        estadistica_visitante.descripcion_encuentro_id = desc_encuentro_visitante 
        estadistica_visitante.save()
        
        messages.success(request, 'Estadísticas guardadas exitosamente')
        
    return render(request, 'asignarEstadisticas.html', {'encuentro': encuentro_obj, 
                                                        'equipoLocal': equipoLocal, 
                                                        'equipoVisita': equipoVisita})


def guardar_estadisticas(encuentro_obj, equipo_obj, estadisticas):
    estadistica_obj = estadisticas(
        encuentro=encuentro_obj,
        equipo=equipo_obj,
        posesion_balon=estadisticas.get('posesion_balon'),
        pases_acertados=estadisticas.get('pases_acertados'),
        tiros_desviados=estadisticas.get('tiros_desviados'),
        efectividad_pases=estadisticas.get('efectividad_pases'),
        tiros_arco=estadisticas.get('tiros_arco'),
        tiros_esquina=estadisticas.get('tiros_esquina')
    )
    estadistica_obj.save()


def asignar_terna_arbitral(request, encuentro_id):
    encuentro_obj = encuentro.objects.get(encuentro_id=encuentro_id)
    arbitros = persona.objects.filter(tipo_persona_id__descripcion='ARBITRO') 
    tipos_arbitro = tipo_arbitro.objects.all()
    detalles_terna = detalle_terna.objects.filter(encuentro_id=encuentro_id)


    
    if request.method == 'POST':
        if 'añadir_detalle' in request.POST:
            # Lógica para guardar los detalles de la terna arbitral
            arbitro_id = int(request.POST.get('arbitro'))
            arbitro = persona.objects.get(persona_id=arbitro_id)
            tipo_arbitro_id = int(request.POST.get('tipo_arbitro'))
            tipo_arbitro_obj = tipo_arbitro.objects.get(tipo_arbitro_id=tipo_arbitro_id)
            
            # Aquí deberías crear un objeto detalle_terna y guardarlo en la base de datos
            detalle = detalle_terna(persona_id=arbitro, tipo_arbitro_id=tipo_arbitro_obj, encuentro_id=encuentro_obj)
            detalle.save()
            messages.success(request, 'Detalle añadido correctamente.')

        elif 'eliminar_detalle' in request.POST:
            # Lógica para eliminar un detalle de la terna arbitral
            detalle_id = int(request.POST.get('eliminar_detalle'))
            detalle = get_object_or_404(detalle_terna, pk=detalle_id)
            detalle.delete()


        return redirect(f"/appPartido/asignar/terna_arbitral/{encuentro_id}/")

    return render(request, 'asignar_terna_arbitral.html', {'encuentro': encuentro_obj, 'arbitros': arbitros, 'tipos_arbitro': tipos_arbitro,'detalles_terna': detalles_terna})

