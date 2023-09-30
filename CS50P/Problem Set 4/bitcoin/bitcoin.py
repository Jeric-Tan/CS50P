import json
import sys
import requests

#If that argument cannot be converted to a float, the program should exit via sys.exit with an error message



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    x = response.json()

    rate = x['bpi']['USD']['rate_float']

    if len(sys.argv) == 2:
        try:
            a = float(sys.argv[1])
            print(a)
            total = rate * float(a)
            print(f'${total:,.4f}')
        except:
            sys.exit('Command-line argument is not a number')
    else:
        sys.exit('Missing command-line argument')


except requests.RequestException:
    sys.exit()