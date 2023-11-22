# Generated by Django 4.1.1 on 2023-11-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0013_remove_organizacion_tipo_remove_pais_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacion',
            name='tipo',
            field=models.CharField(choices=[('F', 'FEDERACIÓN NACIONAL'), ('I', 'FEDERACIÓN INTERNACIONAL'), ('C', 'CONFEDERACIÓN'), ('L', 'LIGA'), ('L', 'ASOCIACIÓN')], default='I', max_length=1),
        ),
    ]
