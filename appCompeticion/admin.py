from django.contrib import admin
from appCompeticion.models import *

# Register your models here.


class competicionAdmin(admin.ModelAdmin):
    list_display=['competicion_id','logo_competicion','deporte_id','nombre','pais_id','organizacion_id']
    ordering=['competicion_id']
    search_fields = ['nombre']

class paisAdmin(admin.ModelAdmin):
    list_display = ['pais_id', 'logo_bandera','nombre','sigla', 'estado']
    ordering = ['pais_id']
    search_fields = ['logo_bandera','nombre','sigla','estado']

class deporteAdmin(admin.ModelAdmin):
    list_display=['deporte_id','nombre','estado']
    ordering=['deporte_id']
    search_fields = ['nombre']

class grupoAdmin(admin.ModelAdmin):
    list_display=['grupo_id','nombre']
    ordering=['grupo_id']
    search_fields = ['nombre']

class faseAdmin(admin.ModelAdmin):
    list_display=['fase_id','nombre']
    ordering=['fase_id']
    search_fields=['nombre']

class detalle_grupoAdmin(admin.ModelAdmin):
    list_display=['detalle_grupo_id','competicion_id','fase_id','grupo_id','equipo_id']
    ordering=['detalle_grupo_id']
    search_fields = ['equipo_id','grupo_id','competicion_id']


class tablaAdmin(admin.ModelAdmin):
    list_display=['tabla_id','competicion_id','equipo_id','ganado','perdido','empatado','goles_favor','goles_contra','tarjetas_amarillas','tarjetas_rojas','puntos']
    ordering=['tabla_id']
    earch_fields = ['competicion_id','equipo_id']
    
class organizacionAdmin(admin.ModelAdmin):
    list_display=['organizacion_id','nombre_oficial','siglas','descripcion','estado','tipo','logo']
    ordering=['organizacion_id']
    earch_fields = ['nombre_oficial']

class patrocinadorAdmin(admin.ModelAdmin):
    list_display=['patrocinador_id','nombre_patrocinador','nombre_abreviado','descripcion','estado','logo_1','logo_2']
    ordering=['nombre_patrocinador']
    search_fields=['nombre_patrocinador','nombre_abreviado']

class detalle_patrocinadorAdmin(admin.ModelAdmin):
    list_display=['patrocinador_id','competicion_id']

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