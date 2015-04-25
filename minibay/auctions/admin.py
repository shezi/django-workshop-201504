from django.contrib import admin

from .models import Auction


class AuctionAdmin(admin.ModelAdmin):

    list_display = (
        'title', 'end_date', 'current_amount_display', 'current_bidder', 'seller',
    )

    
admin.site.register(Auction, AuctionAdmin)
