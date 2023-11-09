from django.contrib import admin
from appContrato.models import *

# Register your models here.
class tipo_personaAdmin(admin.ModelAdmin):
    list_display = ['tipo_persona_id', 'descripcion', 'estado']
    ordering = ['tipo_persona_id']
    search_fields = ['descripcion']

class personaAdmin(admin.ModelAdmin):
    list_display=['persona_id', 'nombre', 'apellido', 'alias', 'sexo', 'fecha_nacimiento','ciudad_id','estatura','peso','tipo_persona_id','estado','foto']
    ordering = ['persona_id']
    search_fields = ['nombre','apellido','alias']
    list_per_page=5
    list_filter=['tipo_persona_id']

class contratoAdmin(admin.ModelAdmin):
    list_display=['contrato_id', 'tipo_persona','persona','tipo_contrato','fecha_inicio', 'fecha_fin', 'valor','nuevo_club','posicion_jugador','dorsal','estado']
    ordering = ['persona']
    search_fields = ['contrato_id','tipo_persona','persona','tipo_contrato']
    
    

class tipoArbitroAdmin(admin.ModelAdmin):
    list_display=['tipo_arbitro_id','nombre','estado']
    ordering=['tipo_arbitro_id']
    search_fields = ['nombre']

class detalleTernaArbitralAdmin(admin.ModelAdmin):
    list_display=['detalle_terna_id','persona_id','tipo_arbitro_id','encuentro_id']
    ordering=['encuentro_id']
    search_fields = ['persona_id','tipo_arbitro_id','encuentro_id']
    list_per_page=5
    list_filter=['tipo_arbitro_id']


admin.site.register(tipo_persona,tipo_personaAdmin)
admin.site.register(persona,personaAdmin)
admin.site.register(contrato,contratoAdmin)
admin.site.register(tipo_arbitro,tipoArbitroAdmin)
admin.site.register(detalle_terna,detalleTernaArbitralAdmin)