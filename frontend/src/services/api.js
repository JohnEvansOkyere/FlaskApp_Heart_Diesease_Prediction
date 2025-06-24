import axios from 'axios';

const API_URL =  process.env.REACT_APP_API_URL;

export const predictHeartDisease = async (data) => {
  try {
    // Transform the data to match backend expectations
    const transformedData = {
      age: data.age,
      sex: data.sex,
      chest_pain_type: data.cp,
      resting_blood_pressure: data.trestbps,
      cholesterol: data.chol,
      fasting_blood_sugar: data.fbs,
      resting_ecg: data.restecg,
      max_heart_rate: data.thalach,
      exercise_angina: data.exang,
      st_depression: data.oldpeak,
      st_slope: data.slope,
      number_of_vessels: data.ca,
      thalassemia: data.thal
    };

    const response = await fetch(`${API_URL}/api/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(transformedData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to get prediction');
    }

    return await response.json();
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
};

export const makePrediction = async (formData) => {
  try {
    const response = await axios.post(`${API_URL}/api/predict`, formData);
    return response.data;
  } catch (error) {
    throw error;
  }
}; 