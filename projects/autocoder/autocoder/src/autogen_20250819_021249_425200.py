from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/bitcoin/latest', methods=['GET'])
def get_latest_bitcoin_price():
    try:
        csv_file = 'bitcoin_prices.csv'
        if not os.path.exists(csv_file):
            return jsonify({'error': 'CSV file not found'}), 404
        
        df = pd.read_csv(csv_file)
        if df.empty:
            return jsonify({'error': 'No data available'}), 404
        
        latest_row = df.iloc[-1]
        
        response = {
            'timestamp': latest_row.get('timestamp', ''),
            'price': float(latest_row.get('price', 0)),
            'currency': 'USD'
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)