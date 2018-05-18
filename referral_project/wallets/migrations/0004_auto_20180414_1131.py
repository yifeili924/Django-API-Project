# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-14 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import referral_project.wallets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0003_auto_20180413_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='kind',
            field=models.IntegerField(choices=[(0, 'Main'), (1, 'Transfer'), (2, 'Referral'), (3, 'External')], default=referral_project.wallets.fields.WalletKind(0)),
        ),
    ]