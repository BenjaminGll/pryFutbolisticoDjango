# Generated by Django 4.1.1 on 2023-11-19 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0019_alter_alineacion_descripcion_encuentro_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuentro_persona',
            name='expulsado',
        ),
        migrations.RemoveField(
            model_name='encuentro_persona',
            name='sustituidos',
        ),
    ]
