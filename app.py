from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model artifacts
model = joblib.load('best_model_xgboost_tuned.pkl')
scaler = joblib.load('scaler.pkl')
feature_cols = joblib.load('feature_cols.pkl')

# Load historical data for lag features
historical_data = pd.read_csv('historical_data.csv')

@app.route('/')
def home():
    return jsonify({
        'message': 'Munich Traffic Accident Prediction API',
        'usage': 'POST to /predict with {"year": 2021, "month": 1}'
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        year = int(data['year'])
        month = int(data['month'])
        
        # Get recent data for lag features
        recent_12 = historical_data.tail(12)
        
        # Create features
        features = {
            'year': year,
            'month': month,
            'month_sin': np.sin(2 * np.pi * month / 12),
            'month_cos': np.cos(2 * np.pi * month / 12),
            'time_idx': (year - 2000) * 12 + month,
            'lag_1': historical_data.iloc[-1]['WERT'],
            'lag_2': historical_data.iloc[-2]['WERT'],
            'lag_3': historical_data.iloc[-3]['WERT'],
            'lag_12': recent_12[recent_12['month'] == month]['WERT'].values[0] if len(recent_12[recent_12['month'] == month]) > 0 else historical_data['WERT'].mean(),
            'rolling_mean_3': historical_data.tail(4).iloc[:-1]['WERT'].mean(),
            'rolling_mean_6': historical_data.tail(7).iloc[:-1]['WERT'].mean(),
            'rolling_std_3': historical_data.tail(4).iloc[:-1]['WERT'].std()
        }
        
        # Prepare and scale
        X = pd.DataFrame([features])[feature_cols]
        X_scaled = scaler.transform(X)
        
        # Predict
        prediction = float(model.predict(X_scaled)[0])
        
        return jsonify({'prediction': round(prediction)})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
