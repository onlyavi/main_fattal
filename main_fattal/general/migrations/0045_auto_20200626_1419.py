# Generated by Django 3.0.7 on 2020-06-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0044_auto_20200626_1417'),
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
            field=models.CharField(blank=True, choices=[('english', 'english'), ('eng_heb', 'engl_heb'), ('full_hebrew', 'full_hebrew')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('linux', 'linux'), ('windows', 'windows')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('c', 'c'), ('b', 'b'), ('other', 'other'), ('a', 'a')], max_length=50, null=True),
        ),
    ]
