# Generated by Django 3.0.8 on 2020-08-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_listing_highestbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='highestbid',
            field=models.IntegerField(default=0),
        ),
    ]