# Generated by Django 4.1.3 on 2022-11-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_purchaserequest_receiver_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaserequest',
            name='nft',
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='nft_token',
            field=models.CharField(default='', editable=False, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nftcollectible',
            name='token',
            field=models.CharField(default='', editable=False, max_length=100, unique=True),
        ),
    ]