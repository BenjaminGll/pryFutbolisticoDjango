# Generated by Django 4.1.1 on 2023-11-11 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0008_alter_organizacion_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalle_grupo',
            options={'verbose_name_plural': 'detalle_grupo'},
        ),
        migrations.AlterModelOptions(
            name='detalle_patrocinador',
            options={'verbose_name_plural': 'Patrocinador_Competicion'},
        ),
    ]
