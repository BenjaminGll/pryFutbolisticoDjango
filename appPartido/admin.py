from django.contrib import admin
from appPartido.models import *


class formacionAdmin(admin.ModelAdmin):
    list_display=['descripcion']
    ordering=['formacion_id']
    search_fields = ['descripcion']
    list_per_page=5
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
class ciudadAdmin(admin.ModelAdmin):
    list_display=['nombre','norma','pais_id']
    ordering=['nombre']
    search_fields = ['nombre']
    list_per_page=5
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)

class sedeAdmin(admin.ModelAdmin):
    list_display=['nombre','alias','capacidad','fecha_inauguracion','ciudad_id', 'imagen','estado']
    ordering=['nombre']
    search_fields = ['nombre']
    list_per_page=5
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
##
class descripcionEncuentroAdmin(admin.ModelAdmin):
    list_display=['encuentro','equipo','goles','goles_ronda_penales','resultado','formacion']
    ordering=['encuentro']
    search_fields = ['encuentro','equipo__nombre', 'encuentro__encuentro_id']
    list_per_page=5
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
class encuentroAdmin(admin.ModelAdmin):
    list_display=['competicion_id','equipo_local','equipo_visita','sede_id','fase','grupo','fecha','clima','estado_jugado']
    ordering=['competicion_id']
    search_fields = ['sede_id__nombre','competicion_id__nombre']
    list_per_page=5
    list_filter=['competicion_id']
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)

# class detalleEncuentroAdmin(admin.ModelAdmin):
#     list_display=['detalle_encuentro_id','encuentro_id','equipo_id','formacion_id','tipo_equipo','resultado']
#     ordering=['detalle_encuentro_id']
#     search_fields=['equipo_id','encuentro_id']

class tipo_eventoAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion','estado','logo_tipo_evento']
    ordering=['nombre']
    search_fields = ['nombre','tipo_evento_id']
    list_per_page=5
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)



class eventoAdmin(admin.ModelAdmin):
    list_display = ['competicion_id', 'tipo_evento_id', 'encuentro_id', 'estado_evento']
    ordering = ['tipo_evento_id']
    search_fields = ['encuentro_id__equipo_local__nombre', 'encuentro_id__equipo_visita__nombre']
    list_filter = ['competicion_id']

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js', 'assets/js/evento_admin.js')
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)


admin.site.register(formacion,formacionAdmin)
admin.site.register(ciudad,ciudadAdmin)
admin.site.register(sede,sedeAdmin)
admin.site.register(descripcion_encuentro,descripcionEncuentroAdmin)
admin.site.register(encuentro,encuentroAdmin)
# admin.site.register(detalle_encuentro,detalleEncuentroAdmin)
admin.site.register(tipo_evento,tipo_eventoAdmin)
admin.site.register(evento,eventoAdmin)