# Generated by Django 3.2.9 on 2022-04-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_newevent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newevent',
            name='discord',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='newevent',
            name='twiter',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='newevent',
            name='website',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
