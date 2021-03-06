# Generated by Django 3.0.6 on 2020-06-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20200615_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfiguration',
            name='gui_kind',
            field=models.CharField(blank=True, choices=[('web', 'web'), ('Tkinter', 'Tkinter')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='lang',
            field=models.CharField(blank=True, choices=[('eng_heb', 'engl_heb'), ('full_hebrew', 'full_hebrew'), ('english', 'english')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('windows', 'windows'), ('linux', 'linux')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('c', 'c'), ('other', 'other'), ('b', 'b'), ('a', 'a')], max_length=50, null=True),
        ),
    ]
