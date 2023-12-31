# Generated by Django 4.1.1 on 2023-11-12 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0019_alter_alineacion_descripcion_encuentro_id'),
        ('appPartido', '0014_evento_competicion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='alineacion1_id',
            field=models.ForeignKey(blank=True, db_column='alineacion_id1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos_alineacion1', to='appEquipo.alineacion'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='alineacion2_id',
            field=models.ForeignKey(blank=True, db_column='alineacion_id2', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos_alineacion2', to='appEquipo.alineacion'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='estado_evento',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tiempo_extra',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tiempo_reglamentario',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
