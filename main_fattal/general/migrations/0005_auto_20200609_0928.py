# Generated by Django 3.0.6 on 2020-06-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20200608_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfiguration',
            name='gui_kind',
            field=models.CharField(blank=True, choices=[('Tkinter', 'Tkinter'), ('web', 'web')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='lang',
            field=models.CharField(blank=True, choices=[('english', 'english'), ('full_hebrew', 'full_hebrew'), ('eng_heb', 'engl_heb')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='os',
            field=models.CharField(blank=True, choices=[('windows', 'windows'), ('linux', 'linux')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='suppliers_name',
            field=models.CharField(blank=True, choices=[('b', 'b'), ('c', 'c'), ('other', 'other'), ('a', 'a')], max_length=50, null=True),
        ),
    ]