# Generated by Django 3.2.9 on 2022-04-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0006_alter_promotenftpromo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchainpromo',
            name='blockp',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='marketplacepromo',
            name='marketp',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
