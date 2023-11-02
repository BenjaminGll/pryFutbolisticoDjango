# Generated by Django 4.1.1 on 2023-11-02 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appContrato', '0002_initial'),
        ('appPartido', '0001_initial'),
        ('appEquipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='sede_id',
            field=models.ForeignKey(db_column='sede_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.sede'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='tipo_equipo_id',
            field=models.ForeignKey(db_column='tipo_equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.tipo_equipo'),
        ),
        migrations.AddField(
            model_name='encuentro_persona',
            name='contrato_id',
            field=models.ForeignKey(db_column='contrato_id', on_delete=django.db.models.deletion.CASCADE, to='appContrato.contrato'),
        ),
        migrations.AddField(
            model_name='encuentro_persona',
            name='equipo_id',
            field=models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.equipo'),
        ),
        migrations.AddField(
            model_name='alineacionequipo',
            name='contrato_id',
            field=models.ForeignKey(db_column='contrato_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='appContrato.contrato'),
        ),
        migrations.AddField(
            model_name='alineacionequipo',
            name='descripcion_encuentro_id',
            field=models.ForeignKey(db_column='descripcion_encuentro_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='appPartido.descripcion_encuentro'),
        ),
        migrations.AddField(
            model_name='alineacionequipo',
            name='posicion_jugador_id',
            field=models.ForeignKey(db_column='posicion_jugador_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='appEquipo.posicion_jugador'),
        ),
    ]
