# Generated by Django 3.0.7 on 2020-07-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history0', '0014_auto_20200706_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='item_unit_kindh',
            field=models.CharField(blank=True, choices=[('units in box', 'unit_in_box'), ('grams', 'grams'), ('liters', 'liters'), ('other', 'other'), ('kg', 'kg')], max_length=50, null=True),
        ),
    ]
