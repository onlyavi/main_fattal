# Generated by Django 3.0.7 on 2020-07-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history0', '0005_auto_20200628_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='item_unit_kindh',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('grams', 'grams'), ('liters', 'liters')], max_length=50, null=True),
        ),
    ]
