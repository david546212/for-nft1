# Generated by Django 3.2.9 on 2022-04-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220412_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newevent',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
