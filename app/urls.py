from django.urls import path
from .views import *

urlpatterns = [
    path('api/address/', ReceiveLocation.as_view(), name='receive_location'),

]
