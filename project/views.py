from calendar import c
from django.shortcuts import get_object_or_404, render
from appContrato.models import *
from appEquipo.models import equipo, alineacion
from appCompeticion.models import (
    competicion,
    deporte,
    detalle_grupo,
    fase,
    grupo,
    tabla_posicion,
)
from appPartido.models import encuentro, evento, sede, tipo_evento
from appCompeticion.models import deporte, organizacion, detalle_grupo,fase
from user.models import User
from django.db.models import Count
from itertools import chain
from django.http import JsonResponse

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import json


def contextoNav():
    deportes = deporte.objects.all()

    data = {"deportes": deportes}

    return render("nav.html", data)


##
# def mostrarEvento(request):

#     eventos = evento.objects.all()
#     # evento_filtrado = evento.objects.filter(evento_id=eventos.evento_id).first()

#     # data_filtrada ={
#     #     'evento' : evento_filtrado
#     # }

#     data ={
#         'eventos' : eventos
#     }

#     return render (request,'moduloTV/evento.html', data)
##
# def mostrarEvento(request):
#     if request.method == 'POST':
#         eventos_seleccionados = request.POST.getlist('idEvento')
#         eventos = evento.objects.filter(evento_id__in=eventos_seleccionados)
#         #return JsonResponse({'eventos': list(eventos.values())})
#         # return render(request, 'tv.html', JsonResponse({'eventos': list(eventos.values())}))
#         obtener_eventos_ajax(eventos)    # Si el método no es POST, simplemente renderiza la página de eventos

#     eventos = evento.objects.all()
#     return render(request, 'moduloTV/evento.html', {'eventos': eventos})

# def obtener_eventos_ajax(eventos):
#     banners = []
#     #if eventos:
#     for evento in eventos:
#             banner = f'''<div class="banner-container">
#                 Tiempo: {evento.tiempo_reglamentario}
#                 </div>'''
#             banners.append(banner)
#     return JsonResponse({'banners': banners})

##


def contadoresAdmin(request):
    arbitros = persona.objects.filter(tipo_persona_id=3).count()
    entrenadores = persona.objects.filter(tipo_persona_id=2).count()
    jugadores = persona.objects.filter(tipo_persona_id=1).count()
    equipos = equipo.objects.count()
    usuarios = User.objects.all()
    data = {
        "arbitros": arbitros,
        "entrenadores": entrenadores,
        "jugadores": jugadores,
        "equipos": equipos,
        "usuarios": usuarios,
    }
    return render(request, "admin/index.html", data)


# def contextoCompetencias(request, nombre_deporte):

#     deportes = deporte.objects.get(nombre=nombre_deporte.upper() ,estado=True)


#     competencia_seleccion = competicion.objects.filter(deporte_id=deportes.deporte_id,tipo_competicion_id=nombre_seleccion, estado=True)

#     competencia_club = competicion.objects.filter(deporte_id=deportes.deporte_id,tipo_competicion_id=nombre_club, estado=True)

#     data= {
#         'deporte' : deportes,
#         'competencia_seleccion' : competencia_seleccion,
#         'competencia_club' : competencia_club
#     }

# return render(request, 'competencias.html', data)


def contextoCompetenciasFutbol(request, nombre_competicion):
    competencia_seleccionada = competicion.objects.get(
        nombre=nombre_competicion.upper(), estado=True
    )
    fase_seleccionada = fase.objects.get(nombre="FASE DE GRUPOS")

    grupos = detalle_grupo.objects.filter(
        competicion_id=competencia_seleccionada.competicion_id,
        fase_id=fase_seleccionada.fase_id,
    ).order_by("grupo_id")

    filtro_grupos = (
        detalle_grupo.objects.filter(
            competicion_id=competencia_seleccionada.competicion_id,
            fase_id=fase_seleccionada.fase_id,
        )
        .values_list("grupo_id", flat=True)
        .distinct()
        .order_by("grupo_id")
    )

    nombre_grupos = []
    for f in filtro_grupos:
        busqueda_grupos = grupo.objects.get(grupo_id=f)
        nombre_grupos.append(busqueda_grupos)

    data = {
        "competencia_seleccionada": competencia_seleccionada,
        "grupos": grupos,
        "nombre_grupos": nombre_grupos,
    }

    return render(request, "teams.html", data)


def contextoJugador(request, alias):
    jugador = persona.objects.get(alias=alias.upper())

    contrato_jugador = contrato.objects.get(
        persona_id=jugador.persona_id, estado=True, tipo_contrato="S"
    )

    lista_contratos_club = []
    contratos_club = contrato.objects.filter(persona_id=jugador, tipo_contrato="C")
    for cc in contratos_club:
        lista_contratos_club.append(cc)

    lista_contratos_seleccion = []
    contratos_seleccion = contrato.objects.filter(persona_id=jugador, tipo_contrato="S")
    for cs in contratos_seleccion:
        lista_contratos_seleccion.append(cs)

    data = {
        "jugador": jugador,
        "contrato": contrato_jugador,
        "contratos_club": lista_contratos_club,
        "contratos_seleccion": lista_contratos_seleccion,
    }

    return render(request, "jugador.html", data)


""" def contextoSedes(request):
    # competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper())   
    # encuentros = encuentro.objects.all().filter(competicion_id=competencia_seleccionada)   
    sedes_competencia=sede.objects.filter(estado='DI')
    data={
        'sedes_competencia': sedes_competencia
    }
    return render(request,'sedes.html',data) """


def obtener_sedes_por_competicion(competicion_id):
    encuentros = encuentro.objects.filter(competicion_id=competicion_id).distinct(
        "sede_id"
    )
    sedes_ids = encuentros.values_list("sede_id", flat=True)
    sedes = sede.objects.filter(sede_id__in=sedes_ids).select_related("ciudad_id")
    return sedes


def contextoSedes(request):
    competiciones = competicion.objects.all()
    competicion_id = request.GET.get("competicionId")
    sedes = (
        obtener_sedes_por_competicion(competicion_id)
        if competicion_id
        else sede.objects.all()
    )

    return render(
        request,
        "ReporteSedeCompeticion.html",
        {
            "competiciones": competiciones,
            "sedes": sedes,
        },
    )

def detalle_sede(request, sede_id):
    sede_instance = get_object_or_404(sede, pk=sede_id)  # Cambia sede_id a pk
    # Aquí puedes agregar más contexto si es necesario
    return render(request, 'detalle_sede.html', {'sede': sede_instance})

def lista_equipos_por_competicion_y_fase(request):
    competiciones = competicion.objects.all()
    fases = fase.objects.all()
    equipos = []
    competicion_seleccionada = None

    competicion_id = request.GET.get('competicion')
    fase_id = request.GET.get('fase')

    if competicion_id:
        competicion_seleccionada = competicion.objects.get(pk=competicion_id)
        if fase_id:
            detalle_grupos = detalle_grupo.objects.filter(competicion_id=competicion_id, fase_id=fase_id)
            equipos = [detalle.equipo_id for detalle in detalle_grupos]

    return render(request, 'ReporteEquiposCompeticion.html', {
        'competiciones': competiciones,
        'fases': fases,
        'equipos': equipos,
        'competicion_seleccionada': competicion_seleccionada,
    })

def contextoEquipo(request, nombre_equipo):
    equipos = equipo.objects.get(nombre=nombre_equipo.upper())
    tipo_persona_entrenador = tipo_persona.objects.get(descripcion="ENTRENADOR")
    persona_entrenador = persona.objects.filter(
        tipo_persona_id=tipo_persona_entrenador.tipo_persona_id
    )

    entrenadoractual = []
    for p_e in persona_entrenador:
        contratosentrenadores = contrato.objects.filter(
            persona_id=p_e.persona_id, nuevo_club=equipos.equipo_id, estado=True
        )
        for ce in contratosentrenadores:
            if ce.estado == True:
                entrenadoractual = ce

    tipo_persona_jugador = tipo_persona.objects.get(descripcion="JUGADOR")
    persona_jugador = persona.objects.filter(
        tipo_persona_id=tipo_persona_jugador.tipo_persona_id
    )

    jugadores_equipo = []
    for p_j in persona_jugador:
        contratosjugadores = contrato.objects.filter(
            persona_id=p_j.persona_id, nuevo_club=equipos.equipo_id, estado=True
        )
        for cj in contratosjugadores:
            if cj.estado == True:
                jugadores_equipo.append(cj)

    # alineacion_equipo_final = []

    # for j in jugadores:
    #     alineacionequipo = alineacion_equipo.objects.filter(contrato_id=j.contrato_id)
    #     for ae in alineacionequipo:
    #         if(ae.estado == True or ae.estado == False):
    #             alineacion_equipo_final.append(ae)
    encuentro_local_jugar = []
    encuentros_local = encuentro.objects.filter(
        equipo_local=equipos.equipo_id, estado_jugado=False
    )
    for ejl in encuentros_local:
        encuentro_local_jugar.append(ejl)

    encuentro_visita_jugar = []
    encuentros_visita = encuentro.objects.filter(
        equipo_visita=equipos.equipo_id, estado_jugado=False
    )
    for ejv in encuentros_visita:
        encuentro_visita_jugar.append(ejv)

    data = {
        "equipo": equipos,
        "entrenador": entrenadoractual,
        "jugadores_equipo": jugadores_equipo,
        "encuentro_local_jugar": encuentro_local_jugar,
        "encuentro_visita_jugar": encuentro_visita_jugar,
    }

    return render(request, "equipo.html", data)


def contextoFixtureCompetencia(request, nombre_competicion):
    competencia_seleccionada = competicion.objects.get(
        nombre=nombre_competicion.upper()
    )

    filtro_encuentros_competencia = encuentro.objects.filter(
        competicion_id=competencia_seleccionada.competicion_id
    )

    # total_detalles_encuentros = detalle_encuentro.objects.all()

    # for de in detalles_encuentros:
    #     for e in filtrar_encuentros_competencias:
    #         if (de.encuentro_id == e.encuentro_id):
    #             lista_detalles_encuentros_competencia.append(de)

    # for f in filtrar_encuentros_competencias:
    #     detalles_encuentros = detalle_encuentro.objects.filter(encuentro_id=f.encuentro_id)
    #     for de in detalles_encuentros:
    #         lista_detalles_encuentros_competencias.append(de)

    data = {
        "competencia": competencia_seleccionada,
        "encuentros": filtro_encuentros_competencia,
    }

    return render(request, "fixtures.html", data)


def contextoListaJugadoresPorGoles(request, nombre_competicion):
    competencia_seleccionada = competicion.objects.get(
        nombre=nombre_competicion.upper()
    )  # FIFA WORLD CUP
    encuentros_competencias = encuentro.objects.filter(
        competicion_id=competencia_seleccionada.competicion_id
    )

    resulta = (
        evento.objects.filter(evento_id=9)
        .filter(encuentro_id__in=encuentros_competencias)
        .values("persona_id")
        .annotate(count=Count("encuentro_evento_id"))
        .order_by("-count")
    )

    lista = [[]]

    i = 0
    for r in resulta:
        li = persona.objects.get(persona_id=r.get("persona_id"))
        lista[i].append(li)
        lista[i].append(r.get("count"))
        if i < len(resulta) - 1:
            lista.append([])
        i = i + 1

    data = {"jugador_goles": lista}
    return render(request, "lista_jugadores_goles.html", data)


# def contextoListaJugadoresPorAmarillas(request,nombre_competicion):
#     competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper()) #FIFA WORLD CUP
#     encuentros_competencias = encuentro.objects.filter(competicion_id=competencia_seleccionada.competicion_id)

#     resulta = evento_persona.objects.filter(evento_id=1).filter(encuentro_id__in=encuentros_competencias).values('persona_id').annotate(count=Count('encuentro_evento_id')).order_by('-count')

#     lista = [[]]

#     i = 0
#     for r in resulta:
#         li = persona.objects.get(persona_id = r.get('persona_id'))
#         lista[i].append(li)
#         lista[i].append(r.get('count'))
#         if i < len(resulta)-1:
#             lista.append([])
#         i = i + 1

#     data={
#         'jugadores_amarillas': lista
#     }

#     return render(request, 'lista_jugadores_amarillas.html', data)

# def contextoListaJugadoresPorRojas(request,nombre_competicion):
#     competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper()) #FIFA WORLD CUP
#     encuentros_competencias = encuentro.objects.filter(competicion_id=competencia_seleccionada.competicion_id)

#     resulta = evento_persona.objects.filter(evento_id=2).filter(encuentro_id__in=encuentros_competencias).values('persona_id').annotate(count=Count('encuentro_evento_id')).order_by('-count')

#     lista = [[]]

#     i = 0
#     for r in resulta:
#         li = persona.objects.get(persona_id = r.get('persona_id'))
#         lista[i].append(li)
#         lista[i].append(r.get('count'))
#         if i < len(resulta)-1:
#             lista.append([])
#         i = i + 1

#     data={
#         'jugadores_rojas': lista
#     }
#     return render(request, 'lista_jugadores_rojas.html', data)

# def contextoListaJugadoresPorAsistencias(request,nombre_competicion):
#     competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper()) #FIFA WORLD CUP
#     encuentros_competencias = encuentro.objects.filter(competicion_id=competencia_seleccionada.competicion_id)

#     resulta = evento_persona.objects.filter(evento_id=19).filter(encuentro_id__in=encuentros_competencias).values('persona_id').annotate(count=Count('encuentro_evento_id')).order_by('-count')

#     lista = [[]]

#     i = 0
#     for r in resulta:
#         li = persona.objects.get(persona_id = r.get('persona_id'))
#         lista[i].append(li)
#         lista[i].append(r.get('count'))
#         if i < len(resulta)-1:
#             lista.append([])
#         i = i + 1

#     data={
#         'jugadores_asistencias': lista
#     }
#     return render(request, 'lista_jugadores_asistencias.html', data)


def contextoTablaPosiciones(request, nombre_competicion):
    competencia_seleccionada = competicion.objects.get(
        nombre=nombre_competicion.upper()
    )

    fase_grupos = fase.objects.get(nombre="FASE DE GRUPOS")
    listar_equipos_fase_grupos = detalle_grupo.objects.filter(
        fase_id=fase_grupos.fase_id
    ).values("equipo_id")

    listar_grupos_fase_grupos = (
        detalle_grupo.objects.filter(fase_id=fase_grupos.fase_id)
        .values_list("grupo_id", flat=True)
        .distinct()
        .order_by("grupo_id")
    )

    nombre_grupos = grupo.objects.filter(grupo_id__in=listar_grupos_fase_grupos)

    lista_tabla = (
        tabla_posicion.objects.filter(
            competicion_id=competencia_seleccionada.competicion_id,
            equipo_id__in=listar_equipos_fase_grupos,
        )
        .values(
            "equipo_id",
            "ganado",
            "empatado",
            "perdido",
            "goles_favor",
            "goles_contra",
            "puntos",
        )
        .order_by("-puntos")
    )

    listaEquipos = [[]]

    i = 0
    posicion = 1

    for c in lista_tabla:
        li = equipo.objects.get(equipo_id=c.get("equipo_id"))
        partidos_jugados = c.get("ganado") + c.get("empatado") + c.get("perdido")
        diferencia_goles = c.get("goles_favor") - c.get("goles_contra")

        listaEquipos[i].append(posicion)  # 0
        listaEquipos[i].append(li.logo)  # 1
        listaEquipos[i].append(li.nombre)  # 2
        listaEquipos[i].append(partidos_jugados)  # 3
        listaEquipos[i].append(c.get("ganado"))  # 4
        listaEquipos[i].append(c.get("empatado"))  # 5
        listaEquipos[i].append(c.get("perdido"))  # 6
        listaEquipos[i].append(c.get("goles_favor"))  # 7
        listaEquipos[i].append(c.get("goles_contra"))  # 8
        listaEquipos[i].append(diferencia_goles)  # 9
        listaEquipos[i].append(c.get("puntos"))  # 10

        if i < len(lista_tabla) - 1:
            listaEquipos.append([])
        i = i + 1
        posicion = posicion + 1

    data = {"equipo": listaEquipos, "listar_grupos_fase_grupos": nombre_grupos}
    return render(request, "tabla-fase.html", data)


def contextoEncuentros(request, nombre_competicion):
    competencia_seleccionada = competicion.objects.get(
        nombre=nombre_competicion.upper()
    )
    encuentros_por_jugar = encuentro.objects.filter(
        competicion_id=competencia_seleccionada, estado_jugado=False
    )
    encuentros_jugados = encuentro.objects.filter(
        competicion_id=competencia_seleccionada, estado_jugado=True
    )
    data = {
        "encuentros_jugados": encuentros_jugados,
        "encuentros_por_jugar": encuentros_por_jugar,
    }
    return render(request, "encuentros_jugados.html", data)


def contextoContacto(request):
    data = {}

    return render(request, "contact.html", data)


def contextoTVvivo(request, id):
    jugar_encuentro = encuentro.objects.get(encuentro_id=id)
    equipo_a = equipo.objects.get(nombre=jugar_encuentro.equipo_local)
    equipo_b = equipo.objects.get(nombre=jugar_encuentro.equipo_visita)

    estadio = sede.objects.get(nombre=jugar_encuentro.sede_id)
    data = {
        "jugar_encuentro": jugar_encuentro,
        "equipo_a": equipo_a,
        "equipo_b": equipo_b,
        "estadio": estadio,
    }

    return render(request, "tvVivo.html", data)


def contextoTVhome(request):
    encuentros = encuentro.objects.filter(estado_jugado=False)
    data = {"encuentros": encuentros}

    return render(request, "tvHome.html", data)


def contextoTv(request, id):
    jugar_encuentro = encuentro.objects.get(encuentro_id=id)
    equipo_a = equipo.objects.get(nombre=jugar_encuentro.equipo_local)
    equipo_b = equipo.objects.get(nombre=jugar_encuentro.equipo_visita)
    estadio = sede.objects.get(nombre=jugar_encuentro.sede_id)
    encuentro_goles = evento.objects.filter(
        encuentro_id=jugar_encuentro.encuentro_id, evento_id=9
    )
    encuentro_tarjetasA = evento.objects.filter(
        encuentro_id=jugar_encuentro.encuentro_id, evento_id=1
    )
    encuentro_tarjetasR = evento.objects.filter(
        encuentro_id=jugar_encuentro.encuentro_id, evento_id=2
    )

    terna_encuentro = detalle_terna.objects.get(
        terna_arbitral_id=jugar_encuentro.terna_arbitral_id_id
    )
    detalle_terna_encuentro = detalle_terna.objects.filter(
        terna_arbitral_id=terna_encuentro.terna_arbitral_id
    ).values("arbitro_id")
    arbitros = persona.objects.filter(arbitro_id__in=detalle_terna_encuentro)

    alineacion_encuentro_a = encuentro.objects.filter(encuentro_id=id).values(
        "alineacion_local"
    )
    alineacion_a = alineacion.objects.filter(
        alineacion_id__in=alineacion_encuentro_a, estado=True
    ).values("alineacion_id")
    detalle_alineacion_a = alineacion.objects.filter(
        alineacion_id__in=alineacion_a, equipo_id=equipo_a.equipo_id
    ).values("contrato_id")
    contrato_alineacion_a = contrato.objects.filter(
        contrato_id__in=detalle_alineacion_a
    ).values("persona_id")
    personas_alineacion_a = persona.objects.filter(persona_id__in=contrato_alineacion_a)

    alineacion_encuentro_b = encuentro.objects.filter(encuentro_id=id).values(
        "alineacion_visita"
    )
    alineacion_b = alineacion.objects.filter(
        alineacion_id__in=alineacion_encuentro_b, estado=True
    ).values("alineacion_id")
    detalle_alineacion_b = alineacion.objects.filter(
        alineacion_id__in=alineacion_b, equipo_id=equipo_b.equipo_id
    ).values("contrato_id")
    contrato_alineacion_b = contrato.objects.filter(
        contrato_id__in=detalle_alineacion_b
    ).values("persona_id")
    personas_alineacion_b = persona.objects.filter(persona_id__in=contrato_alineacion_b)

    data = {
        "jugar_encuentro": jugar_encuentro,
        "equipo_a": equipo_a,
        "equipo_b": equipo_b,
        "estadio": estadio,
        "encuentro_goles": encuentro_goles,
        "encuentro_tarjetasA": encuentro_tarjetasA,
        "encuentro_tarjetasR": encuentro_tarjetasR,
        "arbitros": arbitros,
        "personas_alineacion_a": personas_alineacion_a,
        "personas_alineacion_b": personas_alineacion_b,
    }

    return render(request, "single-result.html", data)


def index(request):
    data = {}
    return render(request, "index.html", data)


def mostrarEvento(request):
    eventos = evento.objects.all()

    if request.method == "POST":
        eventos_seleccionados = request.POST.getlist("idEvento")
        eventos = evento.objects.filter(evento_id__in=eventos_seleccionados)
        guardar_eventos_temporales(eventos)

    return render(request, "moduloTV/evento.html", {"eventos": eventos})


def guardar_eventos_temporales(eventos):
    # Limpiar el archivo temporal existente
    default_storage.delete("eventos_temporales.json")

    # Guardar los eventos en el archivo temporal
    banners = []

    for evento in eventos:
        banner = {
            "html": f'<div class="banner-container">Tiempo: {evento.tiempo_reglamentario}</div>'
        }
        banners.append(banner)

    contenido = json.dumps({"banners": banners})

    default_storage.save("eventos_temporales.json", ContentFile(contenido))


def obtener_eventos_ajax(request):
    eventos_temporales = []

    try:
        with default_storage.open("eventos_temporales.json", "r") as archivo_json:
            eventos_dict = json.load(archivo_json)
            eventos_temporales = eventos_dict["banners"]
    except FileNotFoundError:
        pass

    return JsonResponse({"banners": eventos_temporales})
