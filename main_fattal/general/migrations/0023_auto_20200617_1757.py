# Generated by Django 3.0.6 on 2020-06-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0022_auto_20200617_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfiguration',
            name='gui_kind',
            field=models.CharField(blank=True, choices=[('Tkinter', 'Tkinter'), ('web', 'web')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('linux', 'linux'), ('windows', 'windows')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('c', 'c'), ('other', 'other'), ('b', 'b'), ('a', 'a')], max_length=50, null=True),
        ),
    ]