# Generated by Django 4.1.3 on 2022-11-03 20:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0005_montgomerycountywatershed'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvasivePlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField(blank=True, null=True)),
                ('site_id_fs', models.CharField(blank=True, max_length=30, null=True)),
                ('accepted_p', models.CharField(blank=True, max_length=8, null=True)),
                ('accepted_s', models.CharField(blank=True, max_length=53, null=True)),
                ('accepted_c', models.CharField(blank=True, max_length=60, null=True)),
                ('date_colle', models.DateField(blank=True, null=True)),
                ('total_area', models.FloatField(blank=True, null=True)),
                ('infested_a', models.FloatField(blank=True, null=True)),
                ('infested_p', models.IntegerField(blank=True, null=True)),
                ('fs_unit_na', models.CharField(blank=True, max_length=53, null=True)),
                ('crc_value', models.CharField(blank=True, max_length=16, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
