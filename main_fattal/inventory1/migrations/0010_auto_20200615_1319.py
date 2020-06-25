# Generated by Django 3.0.6 on 2020-06-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0009_auto_20200615_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('units in box', 'unit_in_box'), ('liters', 'liters'), ('grams', 'grams'), ('other', 'other'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('units in box', 'unit_in_box'), ('liters', 'liters'), ('grams', 'grams'), ('other', 'other'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierinformation',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('a', 'a'), ('c', 'c'), ('b', 'b')], max_length=50, null=True),
        ),
    ]
