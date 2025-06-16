from flask import Blueprint, request, jsonify
from ..models.predictor import HeartDiseasePredictor
from ..utils.validation import validate_heart_disease_input

api_bp = Blueprint('api', __name__)
predictor = HeartDiseasePredictor()

@api_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Validate input data
        is_valid, error_message = validate_heart_disease_input(data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        # Convert input data to the correct format
        features = [
            int(data['age']),
            int(data['sex']),
            int(data['chest_pain_type']),
            int(data['resting_blood_pressure']),
            int(data['cholesterol']),
            int(data['fasting_blood_sugar']),
            int(data['resting_ecg']),
            int(data['max_heart_rate']),
            int(data['exercise_angina']),
            float(data['st_depression']),
            int(data['st_slope']),
            int(data['number_of_vessels']),
            int(data['thalassemia'])
        ]
        
        # Make prediction
        prediction = predictor.predict(features)
        probability = predictor.get_prediction_probability(features)
        
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability),
            'message': 'High risk of heart disease' if prediction == 1 else 'Low risk of heart disease'
        })
        
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500 