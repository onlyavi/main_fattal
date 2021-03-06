# Generated by Django 3.0.7 on 2020-07-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0058_auto_20200705_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_fattal_code_issue', models.DecimalField(blank=True, decimal_places=0, default='0', max_digits=1000)),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_quantity_transfer', models.DecimalField(blank=True, decimal_places=0, default='0', max_digits=1000)),
                ('item_name_issue', models.CharField(blank=True, max_length=50, null=True)),
                ('item_transfer_quantity', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('other', 'other'), ('liters', 'liters')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_fattal_code',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('other', 'other'), ('liters', 'liters')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_item_unit_kind',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('units in box', 'unit_in_box'), ('kg', 'kg'), ('other', 'other'), ('liters', 'liters')], max_length=50, null=True),
        ),
    ]
