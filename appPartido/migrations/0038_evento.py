# Generated by Django 4.1.1 on 2023-11-25 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0025_equipo_entrenador_id_tipo_equipo_estado_and_more'),
        ('appPartido', '0037_delete_evento'),
    ]

    operations = [
        migrations.CreateModel(
            name='evento',
            fields=[
                ('evento_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tiempo', models.IntegerField(blank=True, null=True)),
                ('motivo', models.CharField(blank=True, max_length=255, null=True)),
                ('evento_equipo', models.BooleanField()),
                ('alineacion_id1', models.ForeignKey(blank=True, db_column='alineacion_id1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos_alineacion1', to='appEquipo.alineacion')),
                ('alineacion_id2', models.ForeignKey(blank=True, db_column='alineacion_id2', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos_alineacion2', to='appEquipo.alineacion')),
                ('encuentro_id', models.ForeignKey(db_column='encuentro_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='appPartido.encuentro')),
                ('tipo_evento_id', models.ForeignKey(db_column='tipo_evento_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='appPartido.tipo_evento')),
            ],
            options={
                'verbose_name_plural': 'evento',
            },
        ),
    ]
