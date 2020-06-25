# Generated by Django 3.0.6 on 2020-06-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_auto_20200615_1510'),
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
            field=models.CharField(blank=True, choices=[('eng_heb', 'engl_heb'), ('english', 'english'), ('full_hebrew', 'full_hebrew')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('linux', 'linux'), ('windows', 'windows')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('b', 'b'), ('a', 'a'), ('other', 'other'), ('c', 'c')], max_length=50, null=True),
        ),
    ]