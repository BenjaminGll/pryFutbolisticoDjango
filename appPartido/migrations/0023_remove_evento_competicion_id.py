# Generated by Django 4.1.1 on 2023-11-24 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0022_alter_encuentro_resultado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='competicion_id',
        ),
    ]
