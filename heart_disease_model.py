import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import  confusion_matrix
from sklearn.metrics import  accuracy_score
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import joblib
# Loading trained model
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

file_path = get_file_path('heart.csv')


data = pd.read_csv("heart.csv")
#
X = data.drop(columns=['target']) #featured data
y = data['target']  #target data

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Example code to train and save the model (you should replace this with your actual model training code)
# rfc = RandomForestClassifier(n_estimators=500, criterion='entropy', max_depth=8, min_samples_split=5)
# model = rfc.fit(X_train, y_train)
#pickle.dump(model, open('random_forest_model.pkl', 'wb'))

rfc = RandomForestClassifier(n_estimators=500,criterion='entropy',max_depth=8,min_samples_split=5)

#fit the model
model = rfc.fit(X_train, y_train)

# Save the model
with open('random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# print the accuracy
y_pred = model.predict(X_test)
print(f'Test Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%')
# Load the trained model
model = pickle.load(open('random_forest_model.pkl', 'rb'))


def predict_heart_disease(features):
    """
    Predicts heart disease based on input features.

    :param features: A list or array of features for the prediction.
    :return: The prediction (0 or 1).
    """
    features = np.array(features).reshape(1, -1)  # Reshape for a single sample
    prediction = model.predict(features)
    return prediction[0]
