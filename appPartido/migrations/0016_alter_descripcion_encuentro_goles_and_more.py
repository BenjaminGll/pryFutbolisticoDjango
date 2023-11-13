# Generated by Django 4.1.1 on 2023-11-13 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0015_alter_evento_alineacion1_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcion_encuentro',
            name='goles',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='descripcion_encuentro',
            name='resultado',
            field=models.CharField(blank=True, choices=[('G', 'GANADO'), ('E', 'EMPATADO'), ('P', 'PERDIDO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='descripcion_encuentro',
            name='tipo_equipo',
            field=models.CharField(blank=True, choices=[('L', 'LOCAL'), ('V', 'VISITA')], max_length=10, null=True),
        ),
    ]
