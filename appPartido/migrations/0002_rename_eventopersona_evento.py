# Generated by Django 4.1.1 on 2023-11-02 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0003_rename_alineacionequipo_alineacion_and_more'),
        ('appPartido', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='eventoPersona',
            new_name='evento',
        ),
    ]
