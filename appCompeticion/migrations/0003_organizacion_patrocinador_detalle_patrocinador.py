# Generated by Django 4.1.1 on 2023-11-02 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='organizacion',
            fields=[
                ('organizacion_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_oficial', models.CharField(max_length=30)),
                ('siglas', models.CharField(default='', max_length=3)),
                ('descripcion', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('F', 'FEDERACIÓN NACIONAL'), ('I', 'FEDERACIÓN INTERNACIONAL'), ('C', 'CONFEDERACIÓN'), ('L', 'LIGA')], default='I', max_length=1)),
                ('estado', models.BooleanField()),
                ('logo', models.ImageField(blank=True, default='organizacion/bandera_default.png', null=True, upload_to='organizacion/')),
            ],
            options={
                'verbose_name_plural': 'organizaciones',
            },
        ),
        migrations.CreateModel(
            name='patrocinador',
            fields=[
                ('patrocinador_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_patrocinador', models.CharField(max_length=50)),
                ('nombre_abreviado', models.CharField(max_length=10)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField()),
                ('logo_1', models.ImageField(blank=True, default='patrocinador/logo_1/logo_default.png', upload_to='patrocinador/logo_1/')),
                ('logo_2', models.ImageField(blank=True, default='patrocinador/logo_2/logo_default.png', upload_to='patrocinador/logo_2/')),
            ],
            options={
                'verbose_name_plural': 'patrocinador',
            },
        ),
        migrations.CreateModel(
            name='detalle_patrocinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competicion_id', models.ForeignKey(db_column='competicion_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.competicion')),
                ('patrocinador_id', models.ForeignKey(db_column='patrocinador_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.patrocinador')),
            ],
            options={
                'verbose_name_plural': 'detalle_patrocinador',
            },
        ),
    ]
