import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const predictHeartDisease = async (data) => {
  try {
    const response = await fetch(`${API_URL}/api/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('Failed to get prediction');
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