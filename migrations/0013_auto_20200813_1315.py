# Generated by Django 3.0.8 on 2020-08-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200813_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlistitem',
            name='name',
        ),
        migrations.AddField(
            model_name='watchlistitem',
            name='listingid',
            field=models.IntegerField(default=-1),
        ),
    ]
