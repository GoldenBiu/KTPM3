# Generated by Django 5.1.5 on 2025-03-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rename_tongtiendien_chisodiennuoc_giadiencu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chisodiennuoc',
            name='SoDienDaTieuThu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chisodiennuoc',
            name='SoNuocDaTieuThu',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
