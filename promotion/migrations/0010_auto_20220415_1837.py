# Generated by Django 3.2.9 on 2022-04-15 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0009_auto_20220414_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotenftpromo',
            name='blockchain',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='promotion.blockchainpromo'),
        ),
        migrations.AlterField(
            model_name='promotenftpromo',
            name='marketplace',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='promotion.marketplacepromo'),
        ),
    ]
