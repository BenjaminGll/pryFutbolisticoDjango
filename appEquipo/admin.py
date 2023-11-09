from django.contrib import admin
from django.db import models
from django.forms import TextInput, ModelForm
from appEquipo.models import *

# Register your models here.

class categoriaEquipo(admin.ModelAdmin):
    list_display=['nombre']
    ordering=['nombre']
    search_fields=['nombre']

class equipoForm(ModelForm):
    class Meta:
        model = equipo
        exclude = ('deporte_id',)
        widgets = {
            'vestimenta_principal_color_principal': TextInput(attrs={'type': 'color'}),
            'vestimenta_principal_color_secundario': TextInput(attrs={'type': 'color'}),
            'vestimenta_alterna_color_principal': TextInput(attrs={'type': 'color'}),
            'vestimenta_alterna_color_secundario': TextInput(attrs={'type': 'color'}),
        }

class equipoAdmin(admin.ModelAdmin):
    form = equipoForm
    list_display = ['nombre', 'presidente', 'logo', 'vestimenta_principal_color_principal','vestimenta_principal_color_secundario',
                    'vestimenta_alterna_color_principal','vestimenta_alterna_color_secundario', 'portada', 'siglas',
                    'categoria_equipo', 'tipo_equipo_id', 'sede_id']
    ordering = ['nombre']
    search_fields = ['nombre']
    list_per_page=5
    list_filter=['categoria_equipo','tipo_equipo_id']

class tipoEquipoAdmin(admin.ModelAdmin):
    list_display=['descripcion']
    ordering=['tipo_equipo_id']
    search_fields = ['descripcion']

class posicionJugadorAdmin(admin.ModelAdmin):
    list_display=['descripcion']
    ordering=['descripcion']
    search_fields = ['descripcion']
    list_per_page=5

# class alineacionAdmin(admin.ModelAdmin):
#     list_display=['alineacion_id','fecha_juego','descripcion','estado']
#     ordering=['alineacion_id']
#     search_fields=['descripcion']

class AlineacionEquipoAdmin(admin.ModelAdmin):
    list_display=['posicion_jugador_id','dorsal','contrato_id','capitan','estado','descripcion_encuentro_id']
    ordering=['posicion_jugador_id']
    search_fields = ['descripcion_encuentro_id']

class EncuentroPersonaAdmin(admin.ModelAdmin):
     list_display = ['encuentro_persona_id', 'pases', 'asistencias', 'kmrecorridos','pasestotales','pases_acertados', 'pases_errados', 'minutosjugando','expulsado', 'sustituidos', 'amonestado','contrato','encuentro', 'equipo']
     ordering = ['encuentro_persona_id']
     search_fields = ['equipo_id']



admin.site.register(categoria_equipo,categoriaEquipo)
admin.site.register(tipo_equipo,tipoEquipoAdmin)
admin.site.register(equipo,equipoAdmin)
admin.site.register(posicion_jugador,posicionJugadorAdmin)
admin.site.register(alineacion,AlineacionEquipoAdmin)
admin.site.register(encuentro_persona, EncuentroPersonaAdmin)
