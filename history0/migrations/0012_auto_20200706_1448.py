# Generated by Django 3.0.7 on 2020-07-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history0', '0011_auto_20200706_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='item_unit_kindh',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('other', 'other'), ('units in box', 'unit_in_box'), ('liters', 'liters'), ('grams', 'grams')], max_length=50, null=True),
        ),
    ]
