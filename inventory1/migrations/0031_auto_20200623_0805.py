# Generated by Django 3.0.7 on 2020-06-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0030_stock_suppliers_fattal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('liters', 'liters'), ('units in box', 'unit_in_box'), ('other', 'other'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('liters', 'liters'), ('units in box', 'unit_in_box'), ('other', 'other'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('liters', 'liters'), ('units in box', 'unit_in_box'), ('other', 'other'), ('kg', 'kg')], max_length=50, null=True),
        ),
    ]
