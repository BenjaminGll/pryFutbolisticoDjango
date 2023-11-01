from django.contrib import admin
from appArbitro.models import *

# Register your models here.

class tipoArbitroAdmin(admin.ModelAdmin):
    list_display=['arbitro_id','nombre_terna','estado']
    ordering=['arbitro_id']
    search_fields = ['nombre_terna']

class detalleTernaAdmin(admin.ModelAdmin):
    list_display=['detalle_terna_id','tipo_arbitro_id','encuentro_id', 'persona_id']
    ordering=['detalle_terna_id']
    search_fields = ['tipo_arbitro_id']

class ternaArbitralAdmin(admin.ModelAdmin):
    list_display=['terna_arbitral_id','nombre_terna','estado']
    ordering=['terna_arbitral_id']
    search_fields = ['nombre_terna']

class detalleTernaArbitralAdmin(admin.ModelAdmin):
    list_display=['detalle_terna_id','terna_arbitral_id','arbitro_id','tipo_terna_id','estado_juego']
    ordering=['detalle_terna_id']
    search_fields = ['terna_arbitral_id','arbitro_id']

admin.site.register(tipo_arbitro,tipoArbitroAdmin)
admin.site.register(detalle_terna,detalleTernaAdmin)