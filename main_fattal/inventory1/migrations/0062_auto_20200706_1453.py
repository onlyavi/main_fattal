# Generated by Django 3.0.7 on 2020-07-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0061_auto_20200706_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktemp',
            name='formisok',
        ),
        migrations.AddField(
            model_name='stocktemp',
            name='formisokk',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('grams', 'grams'), ('other', 'other'), ('liters', 'liters'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('grams', 'grams'), ('other', 'other'), ('liters', 'liters'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('grams', 'grams'), ('other', 'other'), ('liters', 'liters'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
    ]
