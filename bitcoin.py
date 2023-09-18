import json
import requests
import sys

if (len(sys.argv) != 2):
    sys.exit("Invalid number of cla's")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Invalid cla")
    else:
        while True:
            try:
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                response = response.json()
            except requests.RequestException:
                sys.exit()
            else:
                price = response["bpi"]["USD"]["rate_float"]
                break
    price = "{:.4f}".format(n * price);
    integer_part, decimal_part = price.split(".")
    integer_part = "{:,}".format(int(integer_part))
    price = "$"+integer_part + "." + decimal_part
    print(price)

