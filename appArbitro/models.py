from tabnanny import verbose
from django.db import models

# Create your models here.

class tipo_arbitro(models.Model):

    tipo_arbitro_id = models.BigAutoField(primary_key=True)
    nombre_terna = models.CharField(max_length=50)
    estado = models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        self.nombre_terna = self.nombre_terna.upper()
        super(tipo_arbitro, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.nombre_terna)
    
    class Meta:
        verbose_name_plural='nombre_terna'


class detalle_terna(models.Model):
    detalle_terna_id=models.BigAutoField(primary_key=True)
    tipo_arbitro_id=models.ForeignKey(tipo_arbitro,on_delete=models.CASCADE,db_column='tipo_arbitro_id')
    encuentro_id=models.ForeignKey("appPartido.encuentro",on_delete=models.CASCADE,db_column='encuentro_id')
    persona_id=models.ForeignKey("appContrato.persona",on_delete=models.CASCADE,db_column='persona_id')

    def __str__(self):
        return str(self.detalle_terna_id)        

    class Meta:
        verbose_name_plural='detalle_terna_id'
