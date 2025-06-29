from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load model and features
model = joblib.load('fraud_model.pkl')
features = joblib.load('features.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fraud-detection')
def fraud_detection():
    return render_template('fraud_detection.html', features=features)

@app.route('/model-info')
def model_info():
    return render_template('model_info.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [float(request.form[feature]) for feature in features]
        prediction = model.predict([input_data])[0]
        result_text = "Fraudulent Transaction Detected ❌" if prediction == 1 else "Legitimate Transaction ✅"
        return render_template('result.html', result_text=result_text)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join('uploads', file.filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(filepath)
        df = pd.read_csv(filepath)
        try:
            preds = model.predict(df[features])
            df['Prediction'] = ['Fraud ❌' if p == 1 else 'Legit ✅' for p in preds]
            fraud_count = sum(preds == 1)
            legit_count = sum(preds == 0)
            result_html = df.to_html(classes='table', index=False)
            return render_template('result.html',
                                   result_table=result_html,
                                   fraud_count=fraud_count,
                                   legit_count=legit_count)
        except Exception as e:
            return f"Prediction error: {str(e)}"
    else:
        return "Please upload a valid CSV file."

if __name__ == '__main__':
    app.run(debug=True)
