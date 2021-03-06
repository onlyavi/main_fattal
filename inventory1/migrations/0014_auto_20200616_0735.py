# Generated by Django 3.0.6 on 2020-06-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0013_auto_20200615_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('grams', 'grams'), ('other', 'other'), ('liters', 'liters'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('grams', 'grams'), ('other', 'other'), ('liters', 'liters'), ('units in box', 'unit_in_box')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierinformation',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('b', 'b'), ('a', 'a'), ('other', 'other'), ('c', 'c')], max_length=50, null=True),
        ),
    ]
