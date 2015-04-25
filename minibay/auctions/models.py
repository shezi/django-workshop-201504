from django.db import models
from django.utils import timezone

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
        null=True, blank=True,
    )
    end_date = models.DateTimeField(
        
    )
    seller = models.ForeignKey(
        'auth.User', related_name='sell_auction_set',
    )

    def current_amount_display(self):
        """Gibt die Zahl als Kommazahl mit zwei Nachkommastellen aus."""
        return "{:0.2f}".format(self.current_amount / 100)

    def expired(self):
        """True gdw die Auktion abgelaufen ist."""
        return self.end_date < timezone.now()
