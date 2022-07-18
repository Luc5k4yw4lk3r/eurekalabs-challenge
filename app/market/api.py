from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from market.mixins import AlphaVantageMixinsApi
from market.serializers import PricesSerilizer
from rest_framework.throttling import UserRateThrottle

class CustomUserRateThrottle(UserRateThrottle):
    rate= '10/minute'

class MarketInfo(ListAPIView, AlphaVantageMixinsApi):
    permission_classes = (IsAuthenticated, )
    throttle_classes = [CustomUserRateThrottle]

    def get(self, request, *args, **kwargs):
        r = self.process_request(params=self.request.GET)
        time_series = r.json().get('Time Series (Daily)', None)
        daily_prices = {}
        old_key = None
        variation = 0
        for k, v in time_series.items():
            if old_key:
                variation = float(v.get('4. close', 0)) - old_close
                daily_prices[old_key]['variation'] = '{0:3.4f}'.format(variation)
            old_key = k
            old_close = float(v.get('4. close', 0))
            daily_prices[k] = {
                'open_price': v.get('1. open', None),
                'higher_price': v.get('2. high', None),
                'lower_price': v.get('3. low', None),
            }
        return Response({
            'Time Series (Daily)': daily_prices,
                'Response':'Todo Ok',
        })