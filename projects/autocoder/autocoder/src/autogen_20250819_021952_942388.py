import requests
import csv
import datetime
import os

def fetch_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        price = data['bpi']['USD']['rate_float']
        return price
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

def log_to_csv(price):
    filename = 'bitcoin_price_log.csv'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        if not file_exists:
            writer.writerow(['Timestamp', 'Bitcoin Price (USD)'])
        
        writer.writerow([timestamp, price])

def main():
    price = fetch_bitcoin_price()
    if price is not None:
        log_to_csv(price)
        print(f"Bitcoin price logged: ${price:,.2f}")
    else:
        print("Failed to fetch Bitcoin price")

if __name__ == "__main__":
    main()