import requests
import time
import json
from typing import Optional

def get_bitcoin_price(max_retries: int = 3, retry_delay: int = 2) -> Optional[float]:
    """
    Fetch Bitcoin price with error handling and retries
    """
    apis = [
        "https://api.coindesk.com/v1/bpi/currentprice.json",
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
        "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    ]
    
    for api_url in apis:
        for attempt in range(max_retries):
            try:
                response = requests.get(api_url, timeout=10)
                response.raise_for_status()
                
                data = response.json()
                
                # Parse different API response formats
                if "coindesk.com" in api_url:
                    price = float(data['bpi']['USD']['rate'].replace(',', ''))
                elif "coingecko.com" in api_url:
                    price = float(data['bitcoin']['usd'])
                elif "binance.com" in api_url:
                    price = float(data['price'])
                
                return price
                
            except requests.exceptions.RequestException as e:
                print(f"Request error on attempt {attempt + 1}: {e}")
            except (KeyError, ValueError, TypeError) as e:
                print(f"Data parsing error on attempt {attempt + 1}: {e}")
            except Exception as e:
                print(f"Unexpected error on attempt {attempt + 1}: {e}")
            
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
        
        print(f"Failed to get price from {api_url} after {max_retries} attempts")
    
    print("All APIs failed")
    return None

def main():
    print("Fetching Bitcoin price...")
    price = get_bitcoin_price()
    
    if price:
        print(f"Bitcoin price: ${price:,.2f}")
    else:
        print("Unable to fetch Bitcoin price. Please try again later.")

if __name__ == "__main__":
    main()