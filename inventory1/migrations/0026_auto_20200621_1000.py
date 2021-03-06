# Generated by Django 3.0.7 on 2020-06-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0025_auto_20200621_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('liters', 'liters'), ('kg', 'kg'), ('units in box', 'unit_in_box'), ('grams', 'grams')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('liters', 'liters'), ('kg', 'kg'), ('units in box', 'unit_in_box'), ('grams', 'grams')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierinformation',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('other', 'other')], max_length=50, null=True),
        ),
    ]
