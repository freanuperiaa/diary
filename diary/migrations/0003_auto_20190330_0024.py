# Generated by Django 2.1.7 on 2019-03-30 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20190311_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
