from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

def read_latest_bitcoin_price():
    csv_file = 'bitcoin_prices.csv'
    if not os.path.exists(csv_file):
        return None
    
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if rows:
                return rows[-1]
    except Exception as e:
        return None
    return None

@app.route('/api/bitcoin/latest', methods=['GET'])
def get_latest_bitcoin_price():
    latest_price = read_latest_bitcoin_price()
    if latest_price:
        return jsonify({
            'status': 'success',
            'data': {
                'timestamp': latest_price.get('timestamp'),
                'price': float(latest_price.get('price', 0)),
                'currency': 'USD'
            }
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'No Bitcoin price data available'
        }), 404

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)