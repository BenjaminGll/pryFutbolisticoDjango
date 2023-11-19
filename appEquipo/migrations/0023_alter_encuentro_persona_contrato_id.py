# Generated by Django 4.1.1 on 2023-11-19 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appContrato', '0007_alter_contrato_posicion_jugador'),
        ('appEquipo', '0022_merge_20231119_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro_persona',
            name='contrato_id',
            field=models.ForeignKey(db_column='contrato_id', on_delete=django.db.models.deletion.CASCADE, related_name='encuentro_personas', to='appContrato.contrato'),
        ),
    ]