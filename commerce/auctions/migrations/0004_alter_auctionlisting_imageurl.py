# Generated by Django 3.2.5 on 2022-05-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_auctionlisting_startbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
    ]
