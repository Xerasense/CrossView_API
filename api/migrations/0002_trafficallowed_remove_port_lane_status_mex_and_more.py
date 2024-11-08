# Generated by Django 5.1.3 on 2024-11-08 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficAllowed',
            fields=[
                ('port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.port')),
                ('commercial', models.BooleanField(null=True)),
                ('passenger', models.BooleanField(null=True)),
                ('pedestrian', models.BooleanField(null=True)),
                ('sentri', models.BooleanField(null=True)),
                ('commer_fast', models.BooleanField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='port',
            name='lane_status_mex',
        ),
        migrations.RemoveField(
            model_name='port',
            name='lane_us',
        ),
        migrations.RemoveField(
            model_name='port',
            name='us_lane_type',
        ),
        migrations.AddField(
            model_name='port',
            name='in_estimated_time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='port',
            name='out_estimated_time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='port',
            name='port_status',
            field=models.BooleanField(null=True),
        ),
    ]