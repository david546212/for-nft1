# Generated by Django 3.2.9 on 2022-04-15 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_newevent_blockchain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newevent',
            name='marketplace',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.marketplace'),
        ),
    ]
