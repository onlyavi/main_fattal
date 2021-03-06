# Generated by Django 3.0.7 on 2020-06-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0025_auto_20200621_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfiguration',
            name='lang',
            field=models.CharField(blank=True, choices=[('eng_heb', 'engl_heb'), ('english', 'english'), ('full_hebrew', 'full_hebrew')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('other', 'other'), ('c', 'c'), ('b', 'b')], max_length=50, null=True),
        ),
    ]
