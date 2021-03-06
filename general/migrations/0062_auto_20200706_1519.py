# Generated by Django 3.0.7 on 2020-07-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0061_auto_20200706_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfiguration',
            name='lang',
            field=models.CharField(blank=True, choices=[('english', 'english'), ('full_hebrew', 'full_hebrew'), ('eng_heb', 'engl_heb')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('linux', 'linux'), ('windows', 'windows')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('a', 'a'), ('b', 'b'), ('c', 'c')], max_length=50, null=True),
        ),
    ]
