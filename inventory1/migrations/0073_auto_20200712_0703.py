# Generated by Django 3.0.7 on 2020-07-12 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0072_auto_20200712_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('liters', 'liters'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('grams', 'grams'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('liters', 'liters'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('grams', 'grams'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('liters', 'liters'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('grams', 'grams'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stocktemp',
            name='item_unit_kind_issue',
            field=models.CharField(blank=True, choices=[('liters', 'liters'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('grams', 'grams'), ('other', 'other')], max_length=50, null=True),
        ),
    ]