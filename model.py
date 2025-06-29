import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Train model and save it
def train_and_save_model():
    print("Loading dataset...")
    data = pd.read_csv('creditcard.csv')

    print("Splitting dataset...")
    X = data.drop('Class', axis=1)
    y = data['Class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training model... This may take some time.")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Saving model and features...")
    with open('fraud_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('features.pkl', 'wb') as f:
        pickle.dump(list(X.columns), f)

    print("✅ Model trained and saved as fraud_model.pkl")

# Function to load the model and predict from CSV input file
def predict_csv(csv_file_path):
    # Load features list
    with open('features.pkl', 'rb') as f:
        features = pickle.load(f)

    # Load model
    with open('fraud_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Load new data
    df = pd.read_csv(csv_file_path)

    # Make sure the data has all the required features in correct order
    df = df[features]

    # Predict
    predictions = model.predict(df)

    return predictions
