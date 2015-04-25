# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='current_bidder',
            field=models.ForeignKey(related_name='bid_auction_set', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
