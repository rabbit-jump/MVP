# Generated by Django 3.0.8 on 2020-08-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps_vis', '0004_auto_20200807_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='latitude',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='longitude',
            field=models.TextField(),
        ),
    ]
