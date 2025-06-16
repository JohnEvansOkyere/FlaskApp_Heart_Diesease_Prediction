def validate_heart_disease_input(data):
    """
    Validate the input data for heart disease prediction.
    
    Args:
        data (dict): Input data dictionary
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check required fields
    required_fields = [
        'age', 'sex', 'chest_pain_type', 'resting_blood_pressure',
        'cholesterol', 'fasting_blood_sugar', 'resting_ecg',
        'max_heart_rate', 'exercise_angina', 'st_depression',
        'st_slope', 'number_of_vessels', 'thalassemia'
    ]
    
    for field in required_fields:
        if field not in data:
            return False, f'Missing required field: {field}'
    
    # Validate age
    try:
        age = int(data['age'])
        if not (0 <= age <= 120):
            return False, 'Age must be between 0 and 120'
    except ValueError:
        return False, 'Age must be a valid integer'
    
    # Validate sex
    try:
        sex = int(data['sex'])
        if sex not in [0, 1]:
            return False, 'Sex must be 0 (female) or 1 (male)'
    except ValueError:
        return False, 'Sex must be a valid integer'
    
    # Validate chest pain type
    try:
        chest_pain = int(data['chest_pain_type'])
        if not (0 <= chest_pain <= 3):
            return False, 'Chest pain type must be between 0 and 3'
    except ValueError:
        return False, 'Chest pain type must be a valid integer'
    
    # Validate blood pressure
    try:
        bp = int(data['resting_blood_pressure'])
        if not (0 <= bp <= 300):
            return False, 'Resting blood pressure must be between 0 and 300'
    except ValueError:
        return False, 'Resting blood pressure must be a valid integer'
    
    # Validate cholesterol
    try:
        chol = int(data['cholesterol'])
        if not (0 <= chol <= 600):
            return False, 'Cholesterol must be between 0 and 600'
    except ValueError:
        return False, 'Cholesterol must be a valid integer'
    
    # Validate fasting blood sugar
    try:
        fbs = int(data['fasting_blood_sugar'])
        if fbs not in [0, 1]:
            return False, 'Fasting blood sugar must be 0 or 1'
    except ValueError:
        return False, 'Fasting blood sugar must be a valid integer'
    
    # Validate resting ECG
    try:
        ecg = int(data['resting_ecg'])
        if not (0 <= ecg <= 2):
            return False, 'Resting ECG must be between 0 and 2'
    except ValueError:
        return False, 'Resting ECG must be a valid integer'
    
    # Validate max heart rate
    try:
        hr = int(data['max_heart_rate'])
        if not (0 <= hr <= 300):
            return False, 'Maximum heart rate must be between 0 and 300'
    except ValueError:
        return False, 'Maximum heart rate must be a valid integer'
    
    # Validate exercise angina
    try:
        angina = int(data['exercise_angina'])
        if angina not in [0, 1]:
            return False, 'Exercise angina must be 0 or 1'
    except ValueError:
        return False, 'Exercise angina must be a valid integer'
    
    # Validate ST depression
    try:
        st_dep = float(data['st_depression'])
        if not (0 <= st_dep <= 10):
            return False, 'ST depression must be between 0 and 10'
    except ValueError:
        return False, 'ST depression must be a valid number'
    
    # Validate ST slope
    try:
        slope = int(data['st_slope'])
        if not (0 <= slope <= 2):
            return False, 'ST slope must be between 0 and 2'
    except ValueError:
        return False, 'ST slope must be a valid integer'
    
    # Validate number of vessels
    try:
        vessels = int(data['number_of_vessels'])
        if not (0 <= vessels <= 3):
            return False, 'Number of vessels must be between 0 and 3'
    except ValueError:
        return False, 'Number of vessels must be a valid integer'
    
    # Validate thalassemia
    try:
        thal = int(data['thalassemia'])
        if not (0 <= thal <= 2):
            return False, 'Thalassemia must be between 0 and 2'
    except ValueError:
        return False, 'Thalassemia must be a valid integer'
    
    return True, None 