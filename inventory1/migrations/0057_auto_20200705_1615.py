# Generated by Django 3.0.7 on 2020-07-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0056_auto_20200705_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('units in box', 'unit_in_box'), ('other', 'other'), ('kg', 'kg'), ('liters', 'liters')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('units in box', 'unit_in_box'), ('other', 'other'), ('kg', 'kg'), ('liters', 'liters')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('units in box', 'unit_in_box'), ('other', 'other'), ('kg', 'kg'), ('liters', 'liters')], max_length=50, null=True),
        ),
    ]
