# Generated by Django 5.1.5 on 2025-03-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phong',
            name='DienTich',
            field=models.CharField(max_length=10),
        ),
    ]
