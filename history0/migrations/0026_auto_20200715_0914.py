# Generated by Django 3.0.7 on 2020-07-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history0', '0025_auto_20200712_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='item_unit_kindh',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('kg', 'kg'), ('liters', 'liters'), ('grams', 'grams'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
    ]