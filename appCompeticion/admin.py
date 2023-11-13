from django.contrib import admin
from appCompeticion.models import *

# Register your models here.

class competicionAdmin(admin.ModelAdmin):
    list_display=['nombre','organizacion_id','logo_competicion','deporte_id','pais_id']
    ordering=['nombre']
    search_fields = ['nombre']
    list_filter=['nombre']
    list_per_page=4

class paisAdmin(admin.ModelAdmin):
    list_display = ['nombre','sigla','logo_bandera', 'estado']
    ordering = ['nombre']
    search_fields = ['nombre','sigla','estado']
    list_per_page=6

class deporteAdmin(admin.ModelAdmin):
    list_display=['nombre','estado']
    ordering=['deporte_id']
    search_fields = ['nombre']

class grupoAdmin(admin.ModelAdmin):
    list_display=['nombre']
    ordering=['nombre']
    search_fields = ['nombre']
    list_per_page =4

class faseAdmin(admin.ModelAdmin):
    list_display=['nombre']
    ordering=['nombre']
    search_fields=['nombre']
    list_per_page =4
    

class detalle_grupoAdmin(admin.ModelAdmin):
    list_display=['competicion_id','fase_id','grupo_id','equipo_id']
    search_fields = ['equipo_id','grupo_id','competicion_id']
    ordering =['competicion_id']
    list_per_page =4
    list_filter=['competicion_id']


class tablaAdmin(admin.ModelAdmin):
    list_display=['competicion_id','equipo_id','ganado','perdido','empatado','goles_favor','goles_contra','tarjetas_amarillas','tarjetas_rojas','puntos']
    ordering=['-puntos']
    search_fields = ['competicion_id','equipo_id']
    list_filter=['competicion_id']
    list_per_page=4
    
class organizacionAdmin(admin.ModelAdmin):
    list_display=['nombre_oficial','siglas','tipo','descripcion','estado','logo']
    ordering=['nombre_oficial']
    search_fields = ['nombre_oficial']
    list_per_page=4

class patrocinadorAdmin(admin.ModelAdmin):
    list_display=['nombre_patrocinador','nombre_abreviado','descripcion','estado','logo_1','logo_2']
    ordering=['nombre_patrocinador']
    search_fields=['nombre_patrocinador','nombre_abreviado']
    list_per_page=5

class detalle_patrocinadorAdmin(admin.ModelAdmin):
    list_display=['competicion_id']

admin.site.register(competicion,competicionAdmin)
admin.site.register(pais,paisAdmin)
admin.site.register(deporte,deporteAdmin)
admin.site.register(grupo,grupoAdmin)
admin.site.register(fase,faseAdmin)
admin.site.register(detalle_grupo,detalle_grupoAdmin)
admin.site.register(tabla_posicion,tablaAdmin)
admin.site.register(organizacion,organizacionAdmin)
admin.site.register(patrocinador,patrocinadorAdmin)
admin.site.register(detalle_patrocinador,detalle_patrocinadorAdmin)