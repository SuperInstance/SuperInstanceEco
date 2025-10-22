# bitcoin_logger.py
import requests
import logging
import time
from datetime import datetime
from typing import Optional, Dict, Any

class BitcoinLogger:
    def __init__(self, log_file: str = "bitcoin_prices.log", log_level: int = logging.INFO):
        self.api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        self.logger = self._setup_logger(log_file, log_level)
        
    def _setup_logger(self, log_file: str, log_level: int) -> logging.Logger:
        logger = logging.getLogger("bitcoin_logger")
        logger.setLevel(log_level)
        
        if not logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            
        return logger
    
    def get_bitcoin_price(self) -> Optional[Dict[str, Any]]:
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            price_info = {
                'timestamp': datetime.now().isoformat(),
                'usd_price': data['bpi']['USD']['rate'],
                'usd_rate_float': data['bpi']['USD']['rate_float'],
                'last_updated': data['time']['updated']
            }
            
            return price_info
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch Bitcoin price: {e}")
            return None
        except KeyError as e:
            self.logger.error(f"Unexpected API response format: {e}")
            return None
    
    def log_price(self) -> bool:
        price_info = self.get_bitcoin_price()
        if price_info:
            self.logger.info(
                f"Bitcoin Price: ${price_info['usd_price']} "
                f"(${price_info['usd_rate_float']:.2f}) - "
                f"Last Updated: {price_info['last_updated']}"
            )
            return True
        return False
    
    def start_logging(self, interval_seconds: int = 60):
        self.logger.info("Starting Bitcoin price logging...")
        try:
            while True:
                self.log_price()
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            self.logger.info("Bitcoin price logging stopped by user")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")