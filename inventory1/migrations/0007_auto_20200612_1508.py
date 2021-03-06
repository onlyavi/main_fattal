# Generated by Django 3.0.6 on 2020-06-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0006_auto_20200609_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('grams', 'grams'), ('liters', 'liters'), ('units in box', 'unit_in_box'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('grams', 'grams'), ('liters', 'liters'), ('units in box', 'unit_in_box'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierinformation',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('c', 'c'), ('other', 'other'), ('a', 'a'), ('b', 'b')], max_length=50, null=True),
        ),
    ]
