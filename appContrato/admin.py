from django.contrib import admin
from appContrato.models import *

# Register your models here.
class tipo_personaAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'estado']
    ordering = ['descripcion']
    search_fields = ['descripcion']
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
class personaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'alias', 'sexo', 'fecha_nacimiento', 'ciudad_id', 'estatura', 'peso', 'tipo_persona_id', 'estado', 'foto']
    ordering = ['nombre']
    search_fields = ['nombre', 'apellido', 'alias']
    list_per_page = 6
    list_filter = ['tipo_persona_id', 'contratos_persona__nuevo_club']  # Agrega 'contratos_persona__nuevo_club' a list_filter
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)

class contratoAdmin(admin.ModelAdmin):
    list_display=['tipo_contrato','persona','tipo_persona','fecha_inicio', 'fecha_fin', 'valor','nuevo_club','posicion_jugador','dorsal','estado']
    ordering = ['persona']
    search_fields = ['contrato_id','tipo_persona','persona','tipo_contrato']
    list_filter=['tipo_contrato', 'nuevo_club']
<<<<<<< HEAD
    list_per_page=4
    
=======
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)   
>>>>>>> 1438b181dd410210128b5cc43a7d684283a4cc73

class tipoArbitroAdmin(admin.ModelAdmin):
    list_display=['nombre','estado']
    ordering=['nombre']
    search_fields = ['nombre']
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
class detalleTernaArbitralAdmin(admin.ModelAdmin):
    list_display=['tipo_arbitro_id', 'persona_id','encuentro_id']
    ordering=['encuentro_id']
    search_fields = ['persona_id','tipo_arbitro_id','encuentro_id']
    list_per_page=5
    list_filter=['tipo_arbitro_id']
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)   

admin.site.register(tipo_persona,tipo_personaAdmin)
admin.site.register(persona,personaAdmin)
admin.site.register(contrato,contratoAdmin)
admin.site.register(tipo_arbitro,tipoArbitroAdmin)
admin.site.register(detalle_terna,detalleTernaArbitralAdmin)