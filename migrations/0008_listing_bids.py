# Generated by Django 3.0.8 on 2020-08-01 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20200731_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bids',
            field=models.ManyToManyField(blank=True, related_name='bid', to='auctions.Bid'),
        ),
    ]
