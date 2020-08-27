"""

"""

import requests



class APICaller(object):
    def __init__(self):
        pass
    pass
class FinnhubAPI(APICaller):
    _token: str = None
    API_URL = 'https://finnhub.io/api/v1/'
    maximum_calls_per_second: int = 30

    def __init__(self, token):
        super().__init__()
        self._token = token

        pass

    def get_candlesticks(self, symbol: str, resolution: int, frm: int, to: int):
        """
        Arguments:

        symbolREQUIRED
        Symbol.

        resolutionREQUIRED
        Supported resolution includes 1, 5, 15, 30, 60, D, W, M .Some timeframes might not be available depending on the exchange.

        fromREQUIRED
        UNIX timestamp. Interval initial value.

        toREQUIRED
        UNIX timestamp. Interval end value.

        formatoptional
        By default, format=json. Strings json and csv are accepted.

        adjustedoptional
        By default, adjusted=false. Use true to get adjusted data.

        Response JSON Attributes:

        o
        List of open prices for returned candles.

        h
        List of high prices for returned candles.

        l
        List of low prices for returned candles.

        c
        List of close prices for returned candles.

        v
        List of volume data for returned candles.

        t
        List of timestamp for returned candles.

        s
        Status of the response. This field can either be ok or no_data.

        """
        response = requests.get(f'{self.API_URL}/stock/candle?'
                                f'symbol={symbol}&'
                                f'resolution={resolution}&'
                                f'from={frm}&'
                                f'to={to}&'
                                f'token={self._token}')
        response_json = response.json()
        return response_json


if __name__ == '__main__':
    print(FinnhubAPI('bs2anefrh5rc90r54qqg').get_candlesticks('AAPL', 1, 1598470286, 1598471286))
    pass
