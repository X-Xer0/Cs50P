import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number of bitcoins>")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Invalid number of Bitcoins")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Unable to retrieve Bitcoin price")

    total_cost = bitcoins * price_per_bitcoin
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
