# Generated by Django 3.1.4 on 2021-01-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210106_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.CharField(default='NULL', max_length=64),
        ),
    ]
