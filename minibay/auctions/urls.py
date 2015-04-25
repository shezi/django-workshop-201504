from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'auctions.views.main', name='main'),

    url(r'^auction/(?P<auction_id>\d+)/$',
        'auctions.views.auction_EGAL',
        name='auction_EGAL'),
    
]
