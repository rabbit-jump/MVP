# Generated by Django 3.0.8 on 2020-08-07 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps_vis', '0005_auto_20200807_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='name',
        ),
    ]
