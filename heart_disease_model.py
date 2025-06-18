import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import  confusion_matrix
from sklearn.metrics import  accuracy_score
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import joblib
import os
import sys

def get_file_path(filename):
    if getattr(sys, 'frozen', False):
        # If the application is frozen (i.e., running from a packaged executable)
        base_path = sys._MEIPASS
    else:
        # If running normally (i.e., in a Python environment)
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, filename)

# Only load the model if the pickle file exists
MODEL_PATH = 'random_forest_model.pkl'
model = None
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

def predict_heart_disease(features):
    """
    Predicts heart disease based on input features.

    :param features: A list or array of features for the prediction.
    :return: The prediction (0 or 1).
    """
    if model is None:
        raise RuntimeError('Model is not loaded. Please train the model first.')
    features = np.array(features).reshape(1, -1)  # Reshape for a single sample
    prediction = model.predict(features)
    return prediction[0]

if __name__ == "__main__":
    # Only run this block if the script is executed directly
    file_path = get_file_path('backend/data/heart.csv')
    data = pd.read_csv("backend/data/heart.csv")
    X = data.drop(columns=['target'])
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rfc = RandomForestClassifier(n_estimators=500, criterion='entropy', max_depth=8, min_samples_split=5)
    model = rfc.fit(X_train, y_train)
    with open(MODEL_PATH, 'wb') as model_file:
        pickle.dump(model, model_file)
    y_pred = model.predict(X_test)
    print(f'Test Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%')
