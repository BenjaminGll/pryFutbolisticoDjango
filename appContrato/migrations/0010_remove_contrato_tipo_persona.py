# Generated by Django 4.1.1 on 2023-11-22 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appContrato', '0009_persona_organizacion_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='tipo_persona',
        ),
    ]