# Generated by Django 4.1.3 on 2022-11-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_amount_purchaserequest_amount_spacebucks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nftcollectible',
            name='description',
            field=models.TextField(),
        ),
    ]
