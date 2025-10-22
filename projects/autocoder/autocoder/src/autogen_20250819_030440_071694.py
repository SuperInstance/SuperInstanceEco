import requests
import time
import logging
from datetime import datetime
from typing import Optional

class BitcoinPriceLogger:
    def __init__(self, log_level: int = logging.INFO):
        self.logger = logging.getLogger('bitcoin_price')
        self.logger.setLevel(log_level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def get_bitcoin_price(self) -> Optional[float]:
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', timeout=10)
            response.raise_for_status()
            data = response.json()
            price_str = data['bpi']['USD']['rate'].replace(',', '')
            return float(price_str)
        except requests.RequestException as e:
            self.logger.error(f"Network error fetching Bitcoin price: {e}")
            return None
        except (KeyError, ValueError) as e:
            self.logger.error(f"Error parsing Bitcoin price data: {e}")
            return None
    
    def log_price(self) -> bool:
        price = self.get_bitcoin_price()
        if price is not None:
            self.logger.info(f"Bitcoin price: ${price:,.2f}")
            return True
        else:
            self.logger.warning("Failed to retrieve Bitcoin price")
            return False
    
    def log_prices_continuously(self, interval_seconds: int = 60):
        self.logger.info(f"Starting Bitcoin price logging every {interval_seconds} seconds")
        try:
            while True:
                self.log_price()
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            self.logger.info("Bitcoin price logging stopped by user")
        except Exception as e:
            self.logger.error(f"Unexpected error in price logging: {e}")