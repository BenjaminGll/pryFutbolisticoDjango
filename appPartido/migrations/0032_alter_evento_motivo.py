# Generated by Django 4.1.1 on 2023-11-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0031_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='motivo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
