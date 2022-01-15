from flask import Flask
import stocks
import serverconfig
from auth import authorize

app = Flask(serverconfig.APP_NAME)


@app.route('/api/status', methods=['GET'])
def server_status():
    '''
    Endpoint used to check server status
    '''

    return 'Server is running'


@app.route('/api/price/<symbol>', methods=['GET'])
@authorize
def get_price(symbol):
    '''
    Endpoint used to retrieve the current price for a specific stock symbol
    A secret key (set in advanced) should be present in request's body
    '''

    return str(stocks.get_price(symbol.upper()))


@app.route('/api/price/mock', methods=['GET'])
def get_price_mock():
    '''
    Returns a mocked data
    '''

    return serverconfig.PRICE_MOCK_VALUE


def start_server():
    '''
    Starts Flask server
    '''

    app.run(host=serverconfig.HOST, port=serverconfig.PORT,
            debug=serverconfig.DEBUG)


if __name__ == '__main__':
    '''
    Main method
    '''

    start_server()
