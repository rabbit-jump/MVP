# Generated by Django 3.0.8 on 2020-08-05 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps_vis', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='map_center',
            new_name='Mapcenter',
        ),
        migrations.RenameField(
            model_name='mapcenter',
            old_name='city',
            new_name='cityname',
        ),
    ]