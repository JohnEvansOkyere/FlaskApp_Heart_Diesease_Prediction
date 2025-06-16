import os
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

class HeartDiseasePredictor:
    def __init__(self):
        self.model = None
        self.model_path = os.path.join(os.path.dirname(__file__), '../../models/random_forest_model.pkl')
        self.data_path = os.path.join(os.path.dirname(__file__), '../../data/heart.csv')
        self.load_or_train_model()

    def load_or_train_model(self):
        """Load the trained model or train a new one if it doesn't exist."""
        try:
            self.model = joblib.load(self.model_path)
        except (FileNotFoundError, EOFError):
            self.train_model()

    def train_model(self):
        """Train a new Random Forest model and save it."""
        # Load and preprocess data
        data = pd.read_csv(self.data_path)
        X = data.drop(columns=['target'])
        y = data['target']

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Train the model
        self.model = RandomForestClassifier(
            n_estimators=500,
            criterion='entropy',
            max_depth=8,
            min_samples_split=5,
            random_state=42
        )
        self.model.fit(X_train, y_train)

        # Save the model
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)

    def predict(self, features):
        """
        Make a prediction for the given features.
        
        Args:
            features (list): List of feature values
            
        Returns:
            int: Prediction (0 or 1)
        """
        features = np.array(features).reshape(1, -1)
        return self.model.predict(features)[0]

    def get_prediction_probability(self, features):
        """
        Get the probability of the prediction.
        
        Args:
            features (list): List of feature values
            
        Returns:
            float: Probability of the positive class
        """
        features = np.array(features).reshape(1, -1)
        return self.model.predict_proba(features)[0][1] 