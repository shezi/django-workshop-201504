from django.shortcuts import render


def main(request):
    context = {}
    
    return render(request, 'auctions/main.djhtml', context)
