# Generated by Django 3.0.7 on 2020-07-12 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0071_auto_20200711_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatelist',
            name='Departments',
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('units in box', 'unit_in_box'), ('grams', 'grams'), ('liters', 'liters'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('units in box', 'unit_in_box'), ('grams', 'grams'), ('liters', 'liters'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('units in box', 'unit_in_box'), ('grams', 'grams'), ('liters', 'liters'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stocktemp',
            name='item_unit_kind_issue',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('units in box', 'unit_in_box'), ('grams', 'grams'), ('liters', 'liters'), ('kg', 'kg')], max_length=50, null=True),
        ),
    ]
