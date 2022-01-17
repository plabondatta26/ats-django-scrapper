from django.urls import path
from .views import *

urlpatterns = [
    path('api/address/', ReceiveLocation.as_view(), name='receive_location'),
    # path('', zillow_scrapper, name='zillow_scrapper'),
    # path('/address', zillow_address, name='zillow_address'),
]
