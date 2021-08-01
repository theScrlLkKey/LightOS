import yfinance as yf

Ticker = ''
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


while Ticker != 'exit' or 'quit':
    while Ticker != 'exit' or 'quit':
        Ticker = input('Stock ticker, or exit to quit: ')
        if Ticker.lower() == 'exit' or Ticker.lower() == 'quit':
            exit()
        try:
            csp = float(get_current_price(Ticker))
            print('- '+Ticker.upper() + ': $' + str(round(csp,2)))
        except:
            continue
        csp = 0
    csp = 0