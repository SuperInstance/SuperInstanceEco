from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/bitcoin/latest', methods=['GET'])
def get_latest_bitcoin_price():
    try:
        # Look for CSV file in current directory
        csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
        if not csv_files:
            return jsonify({'error': 'No CSV file found'}), 404
        
        # Use the first CSV file found
        df = pd.read_csv(csv_files[0])
        
        # Get the latest row (assuming data is chronologically ordered)
        latest_row = df.iloc[-1]
        
        # Convert to dictionary and handle NaN values
        latest_data = latest_row.to_dict()
        for key, value in latest_data.items():
            if pd.isna(value):
                latest_data[key] = None
        
        return jsonify(latest_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)