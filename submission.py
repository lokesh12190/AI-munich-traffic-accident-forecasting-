import requests

submission = {
    "github": "https://github.com/lokesh12190/AI-munich-traffic-accident-forecasting-",
    "email": "lkshmetta@gmail.com",
    "url": "https://ai-munich-traffic-accident-forecasting-production.up.railway.app/predict",
    "notes": "XGBoost model with feature engineering (lag features, rolling statistics, cyclical encoding). Deployed on Railway."
}

response = requests.post(
    'https://dps-challenge.netlify.app/.netlify/functions/api/challenge',
    json=submission,
    headers={'Content-Type': 'application/json'}
)

print("Status Code:", response.status_code)
print("Response:", response.json())