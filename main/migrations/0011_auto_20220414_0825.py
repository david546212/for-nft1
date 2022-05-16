# Generated by Django 3.2.9 on 2022-04-14 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220414_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchain',
            name='block',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='market',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='newevent',
            name='blockchain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.blockchain'),
        ),
        migrations.AlterField(
            model_name='newevent',
            name='marketplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.marketplace'),
        ),
    ]
