# Generated by Django 4.1.1 on 2023-11-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0021_alter_encuentro_resultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='resultado',
            field=models.CharField(blank=True, choices=[('L', 'LOCAL'), ('E', 'EMPATE'), ('V', 'VISITA')], max_length=1, null=True),
        ),
    ]
