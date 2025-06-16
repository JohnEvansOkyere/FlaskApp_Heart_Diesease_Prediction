import React, { useState } from 'react';
import { Container, Typography, Box, TextField, Button, Paper } from '@mui/material';
import { predictHeartDisease } from '../services/api';

function Home() {
  const [formData, setFormData] = useState({
    age: '',
    sex: '',
    cp: '',
    trestbps: '',
    chol: '',
    fbs: '',
    restecg: '',
    thalach: '',
    exang: '',
    oldpeak: '',
    slope: '',
    ca: '',
    thal: ''
  });
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const result = await predictHeartDisease(formData);
      setPrediction(result);
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          Heart Disease Prediction
        </Typography>
        <Box component="form" onSubmit={handleSubmit} sx={{ mt: 3 }}>
          <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 2 }}>
            <TextField
              name="age"
              label="Age"
              type="number"
              value={formData.age}
              onChange={handleChange}
              required
            />
            <TextField
              name="sex"
              label="Sex (1 for male, 0 for female)"
              type="number"
              value={formData.sex}
              onChange={handleChange}
              required
            />
            <TextField
              name="cp"
              label="Chest Pain Type (0-3)"
              type="number"
              value={formData.cp}
              onChange={handleChange}
              required
            />
            <TextField
              name="trestbps"
              label="Resting Blood Pressure"
              type="number"
              value={formData.trestbps}
              onChange={handleChange}
              required
            />
            <TextField
              name="chol"
              label="Cholesterol"
              type="number"
              value={formData.chol}
              onChange={handleChange}
              required
            />
            <TextField
              name="fbs"
              label="Fasting Blood Sugar (1 if > 120 mg/dl, 0 otherwise)"
              type="number"
              value={formData.fbs}
              onChange={handleChange}
              required
            />
            <TextField
              name="restecg"
              label="Resting ECG Results (0-2)"
              type="number"
              value={formData.restecg}
              onChange={handleChange}
              required
            />
            <TextField
              name="thalach"
              label="Maximum Heart Rate"
              type="number"
              value={formData.thalach}
              onChange={handleChange}
              required
            />
            <TextField
              name="exang"
              label="Exercise Induced Angina (1 for yes, 0 for no)"
              type="number"
              value={formData.exang}
              onChange={handleChange}
              required
            />
            <TextField
              name="oldpeak"
              label="ST Depression"
              type="number"
              value={formData.oldpeak}
              onChange={handleChange}
              required
            />
            <TextField
              name="slope"
              label="Slope of Peak Exercise ST Segment (0-2)"
              type="number"
              value={formData.slope}
              onChange={handleChange}
              required
            />
            <TextField
              name="ca"
              label="Number of Major Vessels (0-3)"
              type="number"
              value={formData.ca}
              onChange={handleChange}
              required
            />
            <TextField
              name="thal"
              label="Thalassemia (0-2)"
              type="number"
              value={formData.thal}
              onChange={handleChange}
              required
            />
          </Box>
          <Button
            type="submit"
            variant="contained"
            color="primary"
            fullWidth
            sx={{ mt: 3 }}
            disabled={loading}
          >
            {loading ? 'Predicting...' : 'Predict Heart Disease'}
          </Button>
        </Box>
        {prediction !== null && (
          <Box sx={{ mt: 3, textAlign: 'center' }}>
            <Typography variant="h6" color={prediction.prediction === 1 ? 'error' : 'success'}>
              {prediction.prediction === 1
                ? 'High Risk of Heart Disease'
                : 'Low Risk of Heart Disease'}
            </Typography>
            <Typography variant="body1" sx={{ mt: 1 }}>
              Confidence: {(prediction.probability * 100).toFixed(2)}%
            </Typography>
          </Box>
        )}
      </Paper>
    </Container>
  );
}

export default Home; 