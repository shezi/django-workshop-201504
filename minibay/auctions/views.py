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


from django.shortcuts import get_object_or_404, redirect

def auction_EGAL(request, auction_id):
    context = {}
    auction_id = int(auction_id)

    context['auction'] = auction = get_object_or_404(
        Auction,
        id=auction_id,
    )

    if request.method == 'POST':
        if not request.user.is_authenticated():
            context['message'] = 'Geht nur für angemeldete Benutzer!'
        else:
            try:
                bid = int(request.POST['bid'])
                if auction.current_amount >= bid:
                    context['message'] = 'MEHR!!!'
                else:  # auction.current_bid < bid
                    auction.current_amount = bid
                    auction.current_bidder = request.user
                    auction.save()

                    return redirect('.')
                    
            except ValueError:
                context['message'] = 'Bitte geben Sie nur positive Zahlen ein!'
            

    return render(request, 'auctions/auction_EGAL.djhtml', context)
