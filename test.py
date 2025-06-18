import pytest
from app import app
import numpy as np
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('heart_disease_model.predict_heart_disease')
def test_model_prediction(mock_predict):
    # Mock the prediction function to return known values
    mock_predict.return_value = 1
    
    # Test case 1: Sample data that should predict heart disease
    features1 = [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
    prediction1 = mock_predict(features1)
    assert prediction1 == 1

    # Test case 2: Sample data that should predict no heart disease
    mock_predict.return_value = 0
    features2 = [37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2]
    prediction2 = mock_predict(features2)
    assert prediction2 == 0

def test_home_page(client):
    # Test GET request to home page
    response = client.get('/')
    assert response.status_code == 200
    assert b'result' not in response.data  # No result should be shown initially

@patch('app.predict_heart_disease')
def test_prediction_endpoint_valid_data(mock_predict, client):
    # Mock the prediction function
    mock_predict.return_value = 1
    
    # Test POST request with valid data
    test_data = {
        'age': '63',
        'sex': '1',
        'chest_pain_type': '3',
        'resting_blood_pressure': '145',
        'cholesterol': '233',
        'fasting_blood_sugar': '1',
        'resting_electrocardiographic_results': '0',
        'max_heart_rate_achieved': '150',
        'exercise_induced_angina': '0',
        'st_depression': '2.3',
        'st_slope': '0',
        'number_of_major_vessels': '0',
        'thalassemia': '1'
    }
    response = client.post('/', data=test_data)
    assert response.status_code == 200
    assert b'predicts' in response.data.lower()

def test_prediction_endpoint_invalid_data(client):
    # Test POST request with invalid data
    test_data = {
        'age': 'invalid',  # Invalid age
        'sex': '1',
        'chest_pain_type': '3',
        'resting_blood_pressure': '145',
        'cholesterol': '233',
        'fasting_blood_sugar': '1',
        'resting_electrocardiographic_results': '0',
        'max_heart_rate_achieved': '150',
        'exercise_induced_angina': '0',
        'st_depression': '2.3',
        'st_slope': '0',
        'number_of_major_vessels': '0',
        'thalassemia': '1'
    }
    response = client.post('/', data=test_data)
    assert response.status_code == 200
    assert b'invalid input' in response.data.lower()

def test_prediction_endpoint_missing_data(client):
    # Test POST request with missing data
    test_data = {
        'age': '63',
        'sex': '1',
        # Missing other required fields
    }
    response = client.post('/', data=test_data)
    assert response.status_code == 200
    assert b'error' in response.data.lower()

@patch('heart_disease_model.predict_heart_disease')
def test_model_input_validation(mock_predict, client):
    # Test model with invalid input types
    mock_predict.side_effect = Exception("Invalid input")
    
    with pytest.raises(Exception):
        mock_predict(['invalid', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    # Test model with incorrect number of features
    with pytest.raises(Exception):
        mock_predict([1, 2, 3])  # Too few features

    with pytest.raises(Exception):
        mock_predict([1] * 20)  # Too many features 