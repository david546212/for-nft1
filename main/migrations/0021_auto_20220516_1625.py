# Generated by Django 3.2.9 on 2022-05-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20220419_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchain',
            name='block',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='market',
            field=models.CharField(max_length=200),
        ),
    ]
