# Generated by Django 3.0.6 on 2020-06-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_auto_20200615_1308'),
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
            field=models.CharField(blank=True, choices=[('other', 'other'), ('a', 'a'), ('c', 'c'), ('b', 'b')], max_length=50, null=True),
        ),
    ]
