# Generated by Django 3.0.7 on 2020-06-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0050_auto_20200628_1232'),
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
            field=models.CharField(blank=True, choices=[('linux', 'linux'), ('windows', 'windows')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('c', 'c'), ('b', 'b'), ('other', 'other')], max_length=50, null=True),
        ),
    ]
