# Generated by Django 3.0.6 on 2020-06-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0019_auto_20200617_1613'),
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
            field=models.CharField(blank=True, choices=[('full_hebrew', 'full_hebrew'), ('english', 'english'), ('eng_heb', 'engl_heb')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('windows', 'windows'), ('linux', 'linux')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('c', 'c'), ('b', 'b'), ('other', 'other')], max_length=50, null=True),
        ),
    ]
