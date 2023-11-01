from django.contrib import admin
from appPartido.models import *
# Register your models here.

class formacionAdmin(admin.ModelAdmin):
    list_display=['formacion_id','descripcion']
    ordering=['formacion_id']
    search_fields = ['descripcion']

class ciudadAdmin(admin.ModelAdmin):
    list_display=['ciudad_id','nombre','norma','pais_id']
    ordering=['ciudad_id']
    search_fields = ['nombre']

class estadoAdmin(admin.ModelAdmin):
    list_display=['estado_id','nombre']
    ordering=['estado_id']
    search_fields = ['nombre']

class sedeAdmin(admin.ModelAdmin):
    list_display=['sede_id','nombre','alias','capacidad','fecha_inauguracion','ciudad_id', 'imagen','estado']
    ordering=['sede_id']
    search_fields = ['nombre']

class encuentroAdmin(admin.ModelAdmin):
    list_display=['encuentro_id','fase','grupo','alineacion_local','alineacion_visita','equipo_local','equipo_visita','formacion_local','formacion_visita','resultado_local','resultado_visita','resultado_goles_local','resultado_goles_visita','competicion_id','sede_id','terna_arbitral_id','fecha','humedad','clima','estado_jugado']
    ordering=['encuentro_id']
    search_fields = ['equipo_local_id','equipo_visitante_id']

# class detalleEncuentroAdmin(admin.ModelAdmin):
#     list_display=['detalle_encuentro_id','encuentro_id','equipo_id','formacion_id','tipo_equipo','resultado']
#     ordering=['detalle_encuentro_id']
#     search_fields=['equipo_id','encuentro_id']

class tipo_eventoAdmin(admin.ModelAdmin):
    list_display=['tipo_evento_id','nombre','descripcion','estado','logo_tipo_evento']
    ordering=['tipo_evento_id']
    search_fields = ['nombre','tipo_evento_id']

class evento_personaAdmin(admin.ModelAdmin):
    list_display=['encuentro_evento_id','encuentro_id','tipo_evento_id','persona_id','suceso','tipo_suceso','tiempo','observacion'] 
    ordering=['encuentro_evento_id']
    search_fields = ['encuentro_id','persona_id']



admin.site.register(formacion,formacionAdmin)
admin.site.register(estado,estadoAdmin)
admin.site.register(ciudad,ciudadAdmin)
admin.site.register(sede,sedeAdmin)
admin.site.register(encuentro,encuentroAdmin)
# admin.site.register(detalle_encuentro,detalleEncuentroAdmin)
admin.site.register(tipo_evento,tipo_eventoAdmin)
admin.site.register(evento_persona,evento_personaAdmin)