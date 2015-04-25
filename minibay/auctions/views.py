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
