import finnhub
from stocksclientsecrets import FINNHUB_API_KEY


def get_finnhub_client(api_key):
    '''
    Creates a new client using API key
    '''

    return finnhub.Client(api_key)


def get_finnhub_price(client, symbol):
    '''
    Sends a request to Finnhub public API and retrieve the current price for a specific stock symbol

    Finnhub documentation: https://finnhub.io/docs/api/quote
    '''

    return client.quote(symbol)['c']


def get_price(symbol):
    '''
    Returns the current price for the given stock symbol
    '''

    try:
        finnhub_client = get_finnhub_client(FINNHUB_API_KEY)

        return get_finnhub_price(finnhub_client, symbol)
    except Exception as e:
        raise Exception(f'Could not get current price: {e.message}')
