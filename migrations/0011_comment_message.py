# Generated by Django 3.0.8 on 2020-08-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200810_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.CharField(default='NULL', max_length=1024),
        ),
    ]
