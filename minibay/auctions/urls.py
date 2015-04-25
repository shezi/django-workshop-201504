from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'auctions.views.main', name='main'),
    
]
