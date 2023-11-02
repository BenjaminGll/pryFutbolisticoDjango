# Generated by Django 4.1.1 on 2023-11-02 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appEquipo', '0001_initial'),
        ('appCompeticion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabla',
            name='equipo_id',
            field=models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.equipo'),
        ),
        migrations.AddField(
            model_name='detalle_patrocinador',
            name='competicion_id',
            field=models.ForeignKey(db_column='competicion_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.competicion'),
        ),
        migrations.AddField(
            model_name='detalle_patrocinador',
            name='patrocinador_id',
            field=models.ForeignKey(db_column='patrocinador_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.patrocinador'),
        ),
        migrations.AddField(
            model_name='detalle_grupo',
            name='competicion_id',
            field=models.ForeignKey(db_column='competicion_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.competicion'),
        ),
        migrations.AddField(
            model_name='detalle_grupo',
            name='equipo_id',
            field=models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.equipo'),
        ),
        migrations.AddField(
            model_name='detalle_grupo',
            name='fase_id',
            field=models.ForeignKey(db_column='fase_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.fase'),
        ),
        migrations.AddField(
            model_name='detalle_grupo',
            name='grupo_id',
            field=models.ForeignKey(db_column='grupo_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.grupo'),
        ),
        migrations.AddField(
            model_name='competicion',
            name='deporte_id',
            field=models.ForeignKey(db_column='deporte_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.deporte'),
        ),
        migrations.AddField(
            model_name='competicion',
            name='pais_id',
            field=models.ForeignKey(db_column='pais_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.pais'),
        ),
        migrations.AddField(
            model_name='competicion',
            name='tipo_competicion_id',
            field=models.ForeignKey(db_column='tipo_competicion_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.tipo_competicion'),
        ),
    ]
