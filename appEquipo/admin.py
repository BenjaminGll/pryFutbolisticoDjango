from django.contrib import admin
from django.db import models
from django.forms import TextInput, ModelForm
from django.utils.html import format_html
from appEquipo.models import *

# Register your models here.

class categoriaEquipo(admin.ModelAdmin):
    list_display=['nombre']
    ordering=['nombre']
    search_fields=['nombre']
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
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
    def color_vestimenta_principal_principal(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}"></div>',
            obj.vestimenta_principal_color_principal
        )

    def color_vestimenta_principal_secundario(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}"></div>',
            obj.vestimenta_principal_color_secundario
        )

    def color_vestimenta_alterna_principal(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}"></div>',
            obj.vestimenta_alterna_color_principal
        )

    def color_vestimenta_alterna_secundario(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}"></div>',
            obj.vestimenta_alterna_color_secundario
        )
    list_display = ['nombre', 'presidente', 'logo', 'color_vestimenta_principal_principal','color_vestimenta_principal_secundario',
                    'color_vestimenta_alterna_principal','color_vestimenta_alterna_secundario', 'portada', 'siglas',
                    'categoria_equipo', 'tipo_equipo_id', 'sede_id']
    ordering = ['nombre']
    search_fields = ['nombre']
    list_per_page=5
    list_filter=['categoria_equipo','tipo_equipo_id']
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
class tipoEquipoAdmin(admin.ModelAdmin):
    list_display=['descripcion']
    ordering=['tipo_equipo_id']
    search_fields = ['descripcion']
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
class posicionJugadorAdmin(admin.ModelAdmin):
    list_display=['descripcion']
    ordering=['descripcion']
    search_fields = ['descripcion']
    list_per_page=5
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)
# class alineacionAdmin(admin.ModelAdmin):
#     list_display=['alineacion_id','fecha_juego','descripcion','estado']
#     ordering=['alineacion_id']
#     search_fields=['descripcion']

class AlineacionEquipoAdmin(admin.ModelAdmin):
    list_display=['posicion_jugador_id','dorsal','contrato_id','capitan','estado']
    ordering=['posicion_jugador_id']
    search_fields = ['descripcion_encuentro_id']
    list_filter = ['descripcion_encuentro_id__encuentro_id','descripcion_encuentro_id__equipo']
    change_form_template='admin/appEquipo/change_form.html'
    def change_view(self, request, object_id, form_url='', extra_context=None):
    # Obtén el objeto AlineacionEquipo
        alineacion_obj = self.get_object(request, object_id)

        # Filtra los jugadores según el encuentro y el equipo
        jugadores_equipo_izquierdo = alineacion_obj.descripcion_encuentro_id.equipo.descripcion_encuentros.filter(tipo_equipo='L').jugadores.all()
        jugadores_equipo_derecho = alineacion_obj.descripcion_encuentro_id.equipo.descripcion_encuentros.filter(tipo_equipo='V').jugadores.all()

        # Agrega las variables al contexto
        extra_context = extra_context or {}
        extra_context['jugadores_equipo_izquierdo'] = jugadores_equipo_izquierdo
        extra_context['jugadores_equipo_derecho'] = jugadores_equipo_derecho

        return super().change_view(request, object_id, form_url, extra_context)

    # class Media:
    #     js = ('https://code.jquery.com/jquery-3.6.4.min.js', 'assets/js/alineacion_admin.js','assets/js/control_botones.js',)
class EncuentroPersonaAdmin(admin.ModelAdmin):
     list_display = ['encuentro_persona_id', 'pases', 'asistencias', 'kmrecorridos','pasestotales','pases_acertados', 'pases_errados', 'minutosjugando','expulsado', 'sustituidos', 'amonestado','contrato_id','encuentro_id', 'equipo_id']
     ordering = ['encuentro_persona_id']
     search_fields = ['equipo_id']
     class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js','assets/js/control_botones.js',)


admin.site.register(categoria_equipo,categoriaEquipo)
admin.site.register(tipo_equipo,tipoEquipoAdmin)
admin.site.register(equipo,equipoAdmin)
admin.site.register(posicion_jugador,posicionJugadorAdmin)
admin.site.register(alineacion,AlineacionEquipoAdmin)
admin.site.register(encuentro_persona, EncuentroPersonaAdmin)
