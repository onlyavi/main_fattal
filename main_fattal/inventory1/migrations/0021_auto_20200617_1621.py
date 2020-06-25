# Generated by Django 3.0.6 on 2020-06-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0020_auto_20200617_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('units in box', 'unit_in_box'), ('liters', 'liters'), ('other', 'other'), ('grams', 'grams'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('units in box', 'unit_in_box'), ('liters', 'liters'), ('other', 'other'), ('grams', 'grams'), ('kg', 'kg')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierinformation',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('c', 'c'), ('b', 'b'), ('other', 'other')], max_length=50, null=True),
        ),
    ]