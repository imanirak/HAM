# Generated by Django 4.0.3 on 2022-04-21 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_inventory_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='total_stock',
        ),
        migrations.AddField(
            model_name='inventory',
            name='value',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='device',
        ),
        migrations.AddField(
            model_name='inventory',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.device'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(choices=[('MBA', 'MacBook Air'), ('MBP', 'MacBook Pro'), ('S', 'Microsoft Surface')], max_length=50),
        ),
    ]