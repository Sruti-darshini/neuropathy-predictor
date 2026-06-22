from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load the model, scaler, and feature names
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_names = joblib.load('feature_names.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the form
        data = request.json
        
        # Create a dictionary with the correct feature names
        features = {
            'Age': float(data['age']),
            'HbA1c': float(data['hba1c']),
            'FBG': float(data['fbg']),
            '2h-PPBG': float(data['2hppbg']),
            'T.cholesterol': float(data['tcholesterol']),
            'LDL': float(data['ldl']),
            'HDL': float(data['hdl']),
            'TG': float(data['tg']),
            '25(OH)VitD': float(data['vitd']),
            'Ionized Ca': float(data['ionized_ca']),
            'Phosphorus': float(data['phosphorus']),
            'PTH': float(data['pth']),
            'BMI': float(data['bmi'])
        }
        
        # Create DataFrame with correct column order
        input_data = pd.DataFrame([features], columns=feature_names)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        # Prepare response
        result = {
            'prediction': int(prediction),
            'probability': float(probability),
            'status': 'Neuropathic' if prediction == 1 else 'Healthy',
            'confidence': f"{probability * 100:.2f}%" if prediction == 1 else f"{(1 - probability) * 100:.2f}%"
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False') == 'True'
    app.run(debug=debug, port=port, host='0.0.0.0')
