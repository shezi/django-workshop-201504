from django.shortcuts import render
from django.utils import timezone

from .models import Auction


def main(request):
    context = {}

    auctions = Auction.objects.filter(
        end_date__gt=timezone.now()
    ).order_by(
        'end_date', '-current_amount',
    )

    context['auctions'] = auctions

    return render(request, 'auctions/main.djhtml', context)


from django.shortcuts import get_object_or_404

def auction_EGAL(request, auction_id):
    context = {}
    auction_id = int(auction_id)

    context['auction'] = get_object_or_404(
        Auction,
        id=auction_id,
    )

    return render(request, 'auctions/auction_EGAL.djhtml', context)
