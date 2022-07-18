import requests
from django.conf import settings


class AlphaVantageMixinsApi(object):

    def process_request(self, params):
        url = settings.ALPHAVANTAGEAPI_URL
        params = dict(params)
        params.setdefault('function', 'TIME_SERIES_DAILY')
        params.setdefault('apikey', settings.ALPHAVANTAGEAPI_API_KEY)
        r = requests.get(url, params=params)
        return r