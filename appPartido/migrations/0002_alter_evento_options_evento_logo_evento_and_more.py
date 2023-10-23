# Generated by Django 4.1.1 on 2023-10-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name_plural': 'Tipo_evento'},
        ),
        migrations.AddField(
            model_name='evento',
            name='logo_evento',
            field=models.ImageField(blank=True, default='Tipo_evento/logo/logo_default.png', null=True, upload_to='evento/logo/'),
        ),
        migrations.AddField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]