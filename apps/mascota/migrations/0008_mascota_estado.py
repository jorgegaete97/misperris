# Generated by Django 2.1.2 on 2018-11-10 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0007_auto_20181025_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='estado',
            field=models.CharField(choices=[('1', 'Disponible'), ('2', 'No Disponible')], default='1', max_length=1),
        ),
    ]
