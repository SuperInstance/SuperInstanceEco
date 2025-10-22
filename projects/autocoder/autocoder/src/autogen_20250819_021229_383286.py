import requests
import time
import json
from datetime import datetime

def get_bitcoin_price(max_retries=3, retry_delay=2):
    """Fetch Bitcoin price with error handling and retries"""
    
    apis = [
        {
            'url': 'https://api.coindesk.com/v1/bpi/currentprice.json',
            'parser': lambda data: data['bpi']['USD']['rate_float']
        },
        {
            'url': 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
            'parser': lambda data: data['bitcoin']['usd']
        },
        {
            'url': 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT',
            'parser': lambda data: float(data['price'])
        }
    ]
    
    for api in apis:
        for attempt in range(max_retries):
            try:
                response = requests.get(api['url'], timeout=10)
                response.raise_for_status()
                
                data = response.json()
                price = api['parser'](data)
                
                return {
                    'price': price,
                    'timestamp': datetime.now().isoformat(),
                    'source': api['url'],
                    'attempt': attempt + 1
                }
                
            except requests.exceptions.RequestException as e:
                print(f"Request error on attempt {attempt + 1}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay * (attempt + 1))
                    
            except (KeyError, ValueError, json.JSONDecodeError) as e:
                print(f"Data parsing error: {e}")
                break
                
            except Exception as e:
                print(f"Unexpected error: {e}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay * (attempt + 1))
    
    raise Exception("All API sources failed after maximum retries")

def main():
    try:
        result = get_bitcoin_price()
        print(f"Bitcoin Price: ${result['price']:,.2f}")
        print(f"Source: {result['source']}")
        print(f"Retrieved: {result['timestamp']}")
        print(f"Attempts: {result['attempt']}")
        
    except Exception as e:
        print(f"Failed to get Bitcoin price: {e}")
        return None

if __name__ == "__main__":
    main()