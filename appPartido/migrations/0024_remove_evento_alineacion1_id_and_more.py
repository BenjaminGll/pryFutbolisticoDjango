# Generated by Django 4.1.1 on 2023-11-24 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0023_remove_evento_competicion_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='alineacion1_id',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='alineacion2_id',
        ),
    ]
