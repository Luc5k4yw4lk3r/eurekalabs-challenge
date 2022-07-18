from django.urls import path
from market.api import MarketInfo

urlpatterns = [
    path('', MarketInfo.as_view(), name='market'),
]