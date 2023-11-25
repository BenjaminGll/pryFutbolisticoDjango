# Generated by Django 4.1.1 on 2023-11-25 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0014_organizacion_tipo'),
        ('appContrato', '0010_remove_contrato_tipo_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='organizacion_id',
            field=models.ForeignKey(blank=True, db_column='organizacion_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.organizacion'),
        ),
    ]
