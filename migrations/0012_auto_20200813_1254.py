# Generated by Django 3.0.8 on 2020-08-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_comment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='buyer',
            field=models.CharField(max_length=64),
        ),
    ]
