# Generated by Django 4.0.4 on 2022-04-23 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_device_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='value',
        ),
    ]
