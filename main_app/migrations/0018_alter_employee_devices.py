# Generated by Django 4.0.4 on 2022-04-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_remove_device_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='devices',
            field=models.ManyToManyField(blank=True, default='Unassigned', to='main_app.device'),
        ),
    ]
