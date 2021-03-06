# Generated by Django 3.0.6 on 2020-06-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0023_auto_20200617_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('liters', 'liters'), ('other', 'other'), ('units in box', 'unit_in_box'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('liters', 'liters'), ('other', 'other'), ('units in box', 'unit_in_box'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierinformation',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('c', 'c'), ('other', 'other'), ('b', 'b'), ('a', 'a')], max_length=50, null=True),
        ),
    ]
