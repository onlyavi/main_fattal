# Generated by Django 3.0.7 on 2020-06-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0031_auto_20200623_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfiguration',
            name='gui_kind',
            field=models.CharField(blank=True, choices=[('web', 'web'), ('Tkinter', 'Tkinter')], max_length=50, null=True),
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
