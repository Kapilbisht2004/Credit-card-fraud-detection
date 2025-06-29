# 💳 Credit Card Fraud Detection System

A machine learning-powered Flask web application to detect fraudulent transactions in real-time. This project combines a user-friendly interface with the power of a pre-trained model to provide quick and reliable fraud predictions.

---

## 🔍 Key Features

- ✅ **Real-time Prediction** — Enter transaction details manually and detect fraud instantly.
- 📁 **Batch Processing** — Upload a CSV file and analyze multiple transactions in one go.
- 📊 **Visual Output** — See results clearly marked as ✅ Legit or ❌ Fraud.
- 📚 **Model Transparency** — A dedicated section explains how the ML model works.

---

## 🛠️ Tech Stack

| Layer         | Tools/Technologies |
|---------------|--------------------|
| **Frontend**  | HTML, CSS          |
| **Backend**   | Python, Flask      |
| **ML Model**  | Scikit-learn       |
| **Data Handling** | Pandas        |

---

## 🚀 How to Run the Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Kapilbisht2004/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Ensure the following files are present in the project root

fraud_model.pkl – Trained ML model file

features.pkl – Feature transformer for input alignment

Start the Flask app

bash
Copy
Edit
python app.py
