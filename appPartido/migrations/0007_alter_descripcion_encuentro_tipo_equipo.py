# Generated by Django 4.1.1 on 2023-11-05 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0006_evento_estado_evento_alter_encuentro_estado_jugado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcion_encuentro',
            name='resultado',
            field=models.CharField(blank=True, choices=[('G', 'GANADO'), ('E', 'EMPATADO'), ('P', 'PERDIDO')], max_length=2, null=True),
        ),
    ]