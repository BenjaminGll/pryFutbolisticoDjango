# Generated by Django 4.1.1 on 2023-11-02 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0003_organizacion_patrocinador_detalle_patrocinador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='slug',
        ),
    ]
