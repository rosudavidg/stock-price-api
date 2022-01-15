import finnhub
from secrets import FINNHUB_API_KEY


def get_finnhub_client(api_key):

    return finnhub.Client(api_key)


def get_finnhub_price(client, symbol):
    '''
    https://finnhub.io/docs/api/quote
    '''

    return client.quote(symbol)['c']


def get_price(symbol):
    try:
        finnhub_client = get_finnhub_client(FINNHUB_API_KEY)

        return get_finnhub_price(finnhub_client, symbol)
    except Exception as e:
        raise Exception(f'Could not get current price: {e.message}')
