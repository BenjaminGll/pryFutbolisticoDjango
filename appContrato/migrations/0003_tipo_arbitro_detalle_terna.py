# Generated by Django 4.1.1 on 2023-11-02 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0005_merge_20231102_0121'),
        ('appContrato', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_arbitro',
            fields=[
                ('tipo_arbitro_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'tipo_arbitro',
            },
        ),
        migrations.CreateModel(
            name='detalle_terna',
            fields=[
                ('detalle_terna_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('encuentro_id', models.ForeignKey(db_column='encuentro_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.encuentro')),
                ('persona_id', models.ForeignKey(db_column='persona_id', on_delete=django.db.models.deletion.CASCADE, to='appContrato.persona')),
                ('tipo_arbitro_id', models.ForeignKey(db_column='tipo_arbitro_id', on_delete=django.db.models.deletion.CASCADE, to='appContrato.tipo_arbitro')),
            ],
            options={
                'verbose_name_plural': 'detalle_terna',
            },
        ),
    ]