# Generated by Django 3.0.7 on 2020-06-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0049_auto_20200627_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfiguration',
            name='lang',
            field=models.CharField(blank=True, choices=[('eng_heb', 'engl_heb'), ('english', 'english'), ('full_hebrew', 'full_hebrew')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('windows', 'windows'), ('linux', 'linux')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('c', 'c'), ('other', 'other'), ('b', 'b')], max_length=50, null=True),
        ),
    ]
