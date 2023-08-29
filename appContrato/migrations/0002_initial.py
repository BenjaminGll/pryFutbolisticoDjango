# Generated by Django 4.1.1 on 2022-09-30 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appContrato', '0001_initial'),
        ('appEquipo', '0001_initial'),
        ('appPartido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='ciudad_id',
            field=models.ForeignKey(db_column='ciudad_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.ciudad'),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_persona_id',
            field=models.ForeignKey(db_column='tipo_persona_id', on_delete=django.db.models.deletion.CASCADE, to='appContrato.tipo_persona'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='nuevo_club',
            field=models.ForeignKey(blank=True, db_column='nuevo_club', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nuevo_club', to='appEquipo.equipo'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='persona_id',
            field=models.ForeignKey(db_column='persona_id', on_delete=django.db.models.deletion.CASCADE, to='appContrato.persona'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='ultimo_club',
            field=models.ForeignKey(blank=True, db_column='ultimo_club', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ultimo_club', to='appEquipo.equipo'),
        ),
    ]
