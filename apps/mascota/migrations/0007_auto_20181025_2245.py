# Generated by Django 2.1.2 on 2018-10-26 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0006_auto_20181025_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='Foto',
            field=models.ImageField(upload_to='projects'),
        ),
    ]
