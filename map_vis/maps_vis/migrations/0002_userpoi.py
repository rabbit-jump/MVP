# Generated by Django 3.0.9 on 2020-08-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps_vis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userpoi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upoiname', models.CharField(max_length=20)),
                ('upoilog', models.CharField(max_length=20)),
                ('upoilat', models.CharField(max_length=20)),
            ],
        ),
    ]
