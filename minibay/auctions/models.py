from django.db import models

class Auction(models.Model):

    title = models.CharField(
        max_length=103,
    )
    description = models.TextField(
    )
    current_amount = models.BigIntegerField(
    )
    current_bidder = models.ForeignKey(
        'auth.User', related_name='bid_auction_set',
    )
    end_date = models.DateTimeField(
        
    )
    seller = models.ForeignKey(
        'auth.User', related_name='sell_auction_set',
    )
