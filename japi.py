import json
import urllib.request

API_KEY = '&apikey=GNSRZY8KSGMR2IL4'
url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
def getStockData(url, symbol, API_KEY):
        try:
            print ('Searching for Symbol\n')
            connection = urllib.request.urlopen(url + symbol + API_KEY)
            responseString = connection.read().decode()
            return responseString
        except:
            return 'Symbol not found'    



def main():
    try:
        f = open('japi.out', 'x')
    except:
        print ('File exists')

    f = open('japi.out', 'w')
        
    while 1:
        symbol = input ('Please input a stock symbol (type "quit" to quit): ')
        if symbol != 'quit':
            try:
                data = getStockData(url, symbol, API_KEY)
                jdic = json.loads(data)
                output = ('The current price of '+ symbol +' is ' + jdic['Global Quote']['05. price']+'\n')
                print (output)        
                f.write(output)
            except:
                'Symbol not found'
        else:
            f.close()
            raise SystemExit  


if __name__ == '__main__':
    main()
