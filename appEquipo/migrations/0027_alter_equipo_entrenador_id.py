# Generated by Django 4.1.1 on 2023-12-21 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appContrato', '0011_alter_persona_organizacion_id'),
        ('appEquipo', '0026_alter_equipo_entrenador_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='entrenador_id',
            field=models.ForeignKey(blank=True, db_column='contrato_id', limit_choices_to={'persona__tipo_persona_id': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, to='appContrato.contrato'),
        ),
    ]
