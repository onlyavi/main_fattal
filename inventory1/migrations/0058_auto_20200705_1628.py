# Generated by Django 3.0.7 on 2020-07-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0057_auto_20200705_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('liters', 'liters'), ('other', 'other'), ('grams', 'grams'), ('kg', 'kg'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('liters', 'liters'), ('other', 'other'), ('grams', 'grams'), ('kg', 'kg'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('liters', 'liters'), ('other', 'other'), ('grams', 'grams'), ('kg', 'kg'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
    ]
