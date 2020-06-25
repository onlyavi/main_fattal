# Generated by Django 3.0.7 on 2020-06-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0037_auto_20200624_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('kg', 'kg'), ('units in box', 'unit_in_box'), ('liters', 'liters'), ('grams', 'grams')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('kg', 'kg'), ('units in box', 'unit_in_box'), ('liters', 'liters'), ('grams', 'grams')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('kg', 'kg'), ('units in box', 'unit_in_box'), ('liters', 'liters'), ('grams', 'grams')], max_length=50, null=True),
        ),
    ]