class descripcion_encuentro(models.Model):
    CHOICE_RESULTADO = [
        ('G', 'GANADO'),
        ('E', 'EMPATADO'),
        ('P', 'PERDIDO'),
    ]
    descripcion_encuentro_id = models.BigAutoField(primary_key=True)
    goles = models.CharField(max_length=4)
    goles_ronda_penales = models.CharField(max_length=4)
    resultado = models.CharField(max_length=1, choices=CHOICE_RESULTADO)
    formacion = models.ForeignKey('formacion', on_delete=models.CASCADE, db_column='formacion_id', related_name='descripcion_encuentros', blank=True, null=True)
    equipo = models.ForeignKey('appEquipo.equipo', on_delete=models.CASCADE, db_column='equipo_id', related_name='descripcion_encuentros', blank=True, null=True)
    encuentro = models.ForeignKey('encuentro', on_delete=models.CASCADE, db_column='encuentro_id', related_name='descripcion_encuentros', blank=True, null=True)

    def save(self, force_insert=False, force_update=False):
        super(descripcion_encuentro, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = 'descripcion_encuentro'


##FIN_NUEVO
class encuentro(models.Model):
    # CHOICE_RESULTADO = [
    #     ('G', 'GANADO'),
    #     ('E', 'EMPATADO'),
    #     ('P', 'PERDIDO'),
    # ]

    encuentro_id=models.BigAutoField(primary_key=True)
    competicion_id=models.ForeignKey("appCompeticion.competicion", on_delete=models.CASCADE,db_column='competicion_id')
    sede_id=models.ForeignKey(sede,on_delete=models.CASCADE,db_column='sede_id',blank=True,null=True)
    fase=models.ForeignKey("appCompeticion.fase", on_delete=models.CASCADE,db_column='fase',related_name='fase')
    grupo=models.ForeignKey("appCompeticion.grupo", on_delete=models.CASCADE,db_column='grupo',related_name='grupo')
    equipo_local=models.ForeignKey('appEquipo.equipo', on_delete=models.CASCADE,db_column='equipo_local',related_name='equipo_local')
    equipo_visita=models.ForeignKey('appEquipo.equipo', on_delete=models.CASCADE,db_column='equipo_visita',related_name='equipo_visita')
    fecha=models.DateTimeField(blank=True,null=True)
    clima=models.CharField(max_length=4)
    estado_jugado=models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        
        self.clima = self.clima.upper()
        super(encuentro, self).save(force_insert, force_update)
        ##
                        # Crear registros en descripcion_encuentro
        descripcion_local = descripcion_encuentro(
            encuentro_id=self.encuentro_id,
            equipo_id=self.equipo_local,
        )
        descripcion_local.save(force_insert, force_update)

        descripcion_visita = descripcion_encuentro(
            encuentro_id=self.encuentro_id,
            equipo_id=self.equipo_visita,
        )
        descripcion_visita.save(force_insert, force_update)


        ##
    def __str__(self):
        return str(self.equipo_local) + " vs " + str(self.equipo_visita)
        
    class Meta:
        verbose_name_plural = 'encuentro'




class descripcionEncuentroAdmin(admin.ModelAdmin):
    list_display=['descripcion_encuentro_id','goles','goles_ronda_penales','resultado','formacion_id','equipo_id','encuentro_id']
    ordering=['descripcion_encuentro_id']
    search_fields = ['equipo_id','encuentro_id']
##
class encuentroAdmin(admin.ModelAdmin):
    list_display=['encuentro_id','competicion_id','sede_id','fase','grupo','equipo_local','equipo_visita','fecha','clima','estado_jugado']
    ordering=['encuentro_id']
    search_fields = ['sede_id','competicion_id']