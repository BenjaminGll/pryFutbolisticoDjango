# Generated by Django 4.1.1 on 2023-11-02 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appContrato', '0002_initial'),
        ('appEquipo', '0006_merge_0004_alter_equipo_deporte_id_0005_alineacion'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='encuentro_persona',
            unique_together={('contrato_id', 'encuentro_id', 'equipo_id')},
        ),
    ]
