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
    list_display=['sede_id','nombre','alias','capacidad','fecha_inauguracion','ciudad_id','estado']
    ordering=['sede_id']
    search_fields = ['nombre']

##
class descripcionEncuentroAdmin(admin.ModelAdmin):
    list_display=['descripcion_encuentro_id','goles','goles_ronda_penales','resultado','formacion','equipo','encuentro']
    ordering=['descripcion_encuentro_id']
    search_fields = ['equipo__nombre', 'encuentro__encuentro_id']

class encuentroAdmin(admin.ModelAdmin):
    list_display=['encuentro_id','competicion_id','sede_id','fase','grupo','fecha','clima','estado_jugado']
    ordering=['encuentro_id']
    search_fields = ['sede_id__nombre','competicion_id__nombre']


# class detalleEncuentroAdmin(admin.ModelAdmin):
#     list_display=['detalle_encuentro_id','encuentro_id','equipo_id','formacion_id','tipo_equipo','resultado']
#     ordering=['detalle_encuentro_id']
#     search_fields=['equipo_id','encuentro_id']

class eventoAdmin(admin.ModelAdmin):
    list_display=['evento_id','descripcion','estado']
    ordering=['evento_id']
    search_fields = ['descripcion']

class evento_personaAdmin(admin.ModelAdmin):
    list_display=['encuentro_evento_id','encuentro_id','evento_id','persona_id','suceso','tipo_suceso','tiempo','observacion'] 
    ordering=['encuentro_evento_id']
    search_fields = ['encuentro_id','persona_id']



admin.site.register(formacion,formacionAdmin)
admin.site.register(estado,estadoAdmin)
admin.site.register(ciudad,ciudadAdmin)
admin.site.register(sede,sedeAdmin)
admin.site.register(descripcion_encuentro,descripcionEncuentroAdmin)
admin.site.register(encuentro,encuentroAdmin)
# admin.site.register(detalle_encuentro,detalleEncuentroAdmin)
admin.site.register(evento,eventoAdmin)
admin.site.register(evento_persona,evento_personaAdmin)