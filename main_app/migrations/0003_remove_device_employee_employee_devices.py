# Generated by Django 4.0.3 on 2022-04-19 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='devices',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.device'),
        ),
    ]