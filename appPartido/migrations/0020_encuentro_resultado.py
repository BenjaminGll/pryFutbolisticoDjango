# Generated by Django 4.1.1 on 2023-11-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0019_rename_tiempo_extra_evento_tiempo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuentro',
            name='resultado',
            field=models.CharField(choices=[('L', 'LOCAL'), ('E', 'EMPATE'), ('V', 'VISITA')], default='E', max_length=1, null=True),
        ),
    ]
