import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

def evaluate_model(model_path, test_data_path):
    # Load the trained model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Load test data
    data = pd.read_csv(test_data_path)
    X_test = data.drop(columns=['target'])
    y_test = data['target']
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Print results
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model('random_forest_model.pkl', 'backend/data/heart.csv') 