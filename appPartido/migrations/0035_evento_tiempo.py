# Generated by Django 4.1.1 on 2023-11-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0034_remove_evento_tiempo'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='tiempo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
