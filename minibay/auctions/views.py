from django.shortcuts import render

from .models import Auction


def main(request):
    context = {}

    auctions = Auction.objects.all()
    context['auctions'] = auctions
    
    return render(request, 'auctions/main.djhtml', context)
