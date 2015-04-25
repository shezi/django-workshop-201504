# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=103)),
                ('description', models.TextField()),
                ('current_amount', models.BigIntegerField()),
                ('end_date', models.DateTimeField()),
                ('current_bidder', models.ForeignKey(related_name='bid_auction_set', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(related_name='sell_auction_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
