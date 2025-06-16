import React, { useState } from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  TextField, 
  Button, 
  Paper, 
  FormHelperText,
  Select,
  MenuItem,
  InputLabel,
  FormControl
} from '@mui/material';
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

  const [errors, setErrors] = useState({});
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const validateField = (name, value) => {
    switch (name) {
      case 'age':
        return value >= 0 && value <= 120 ? '' : 'Age must be between 0 and 120';
      case 'sex':
        return value === '0' || value === '1' ? '' : 'Please select a valid option';
      case 'cp':
        return value === '0' || value === '1' || value === '2' || value === '3' ? '' : 'Please select a valid option';
      case 'trestbps':
        return value >= 0 && value <= 300 ? '' : 'Resting blood pressure must be between 0 and 300 mmHg';
      case 'chol':
        return value >= 0 && value <= 600 ? '' : 'Cholesterol must be between 0 and 600 mg/dl';
      case 'fbs':
        return value === '0' || value === '1' ? '' : 'Please select a valid option';
      case 'restecg':
        return value === '0' || value === '1' || value === '2' ? '' : 'Please select a valid option';
      case 'thalach':
        return value >= 0 && value <= 300 ? '' : 'Maximum heart rate must be between 0 and 300 bpm';
      case 'exang':
        return value === '0' || value === '1' ? '' : 'Please select a valid option';
      case 'oldpeak':
        return value >= 0 && value <= 10 ? '' : 'ST depression must be between 0 and 10 mm';
      case 'slope':
        return value === '0' || value === '1' || value === '2' ? '' : 'Please select a valid option';
      case 'ca':
        return value === '0' || value === '1' || value === '2' || value === '3' ? '' : 'Please select a valid option';
      case 'thal':
        return value === '0' || value === '1' || value === '2' ? '' : 'Please select a valid option';
      default:
        return '';
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    const error = validateField(name, value);
    setErrors({
      ...errors,
      [name]: error
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newErrors = {};
    Object.keys(formData).forEach(key => {
      const error = validateField(key, formData[key]);
      if (error) newErrors[key] = error;
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

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
            {/* Numerical Inputs */}
            <TextField
              name="age"
              label="Age"
              type="number"
              value={formData.age}
              onChange={handleChange}
              error={!!errors.age}
              helperText={errors.age || "Enter age in years (0-120)"}
              required
              inputProps={{ min: 0, max: 120 }}
            />
            <TextField
              name="trestbps"
              label="Resting Blood Pressure"
              type="number"
              value={formData.trestbps}
              onChange={handleChange}
              error={!!errors.trestbps}
              helperText={errors.trestbps || "Enter in mmHg (0-300)"}
              required
              inputProps={{ min: 0, max: 300 }}
            />
            <TextField
              name="chol"
              label="Cholesterol"
              type="number"
              value={formData.chol}
              onChange={handleChange}
              error={!!errors.chol}
              helperText={errors.chol || "Enter in mg/dl (0-600)"}
              required
              inputProps={{ min: 0, max: 600 }}
            />
            <TextField
              name="thalach"
              label="Maximum Heart Rate"
              type="number"
              value={formData.thalach}
              onChange={handleChange}
              error={!!errors.thalach}
              helperText={errors.thalach || "Enter in bpm (0-300)"}
              required
              inputProps={{ min: 0, max: 300 }}
            />
            <TextField
              name="oldpeak"
              label="ST Depression"
              type="number"
              value={formData.oldpeak}
              onChange={handleChange}
              error={!!errors.oldpeak}
              helperText={errors.oldpeak || "Enter in mm (0-10)"}
              required
              inputProps={{ min: 0, max: 10, step: 0.1 }}
            />

            {/* Categorical Inputs */}
            <FormControl fullWidth error={!!errors.sex}>
              <InputLabel>Sex</InputLabel>
              <Select
                name="sex"
                value={formData.sex}
                onChange={handleChange}
                label="Sex"
                required
              >
                <MenuItem value="0">Female</MenuItem>
                <MenuItem value="1">Male</MenuItem>
              </Select>
              {errors.sex && <FormHelperText>{errors.sex}</FormHelperText>}
            </FormControl>

            <FormControl fullWidth error={!!errors.cp}>
              <InputLabel>Chest Pain Type</InputLabel>
              <Select
                name="cp"
                value={formData.cp}
                onChange={handleChange}
                label="Chest Pain Type"
                required
              >
                <MenuItem value="0">Typical Angina</MenuItem>
                <MenuItem value="1">Atypical Angina</MenuItem>
                <MenuItem value="2">Non-anginal Pain</MenuItem>
                <MenuItem value="3">Asymptomatic</MenuItem>
              </Select>
              {errors.cp && <FormHelperText>{errors.cp}</FormHelperText>}
            </FormControl>

            <FormControl fullWidth error={!!errors.fbs}>
              <InputLabel>Fasting Blood Sugar</InputLabel>
              <Select
                name="fbs"
                value={formData.fbs}
                onChange={handleChange}
                label="Fasting Blood Sugar"
                required
              >
                <MenuItem value="0">≤ 120 mg/dl</MenuItem>
                <MenuItem value="1">> 120 mg/dl</MenuItem>
              </Select>
              {errors.fbs && <FormHelperText>{errors.fbs}</FormHelperText>}
            </FormControl>

            <FormControl fullWidth error={!!errors.restecg}>
              <InputLabel>Resting ECG Results</InputLabel>
              <Select
                name="restecg"
                value={formData.restecg}
                onChange={handleChange}
                label="Resting ECG Results"
                required
              >
                <MenuItem value="0">Normal</MenuItem>
                <MenuItem value="1">ST-T Wave Abnormality</MenuItem>
                <MenuItem value="2">Left Ventricular Hypertrophy</MenuItem>
              </Select>
              {errors.restecg && <FormHelperText>{errors.restecg}</FormHelperText>}
            </FormControl>

            <FormControl fullWidth error={!!errors.exang}>
              <InputLabel>Exercise Induced Angina</InputLabel>
              <Select
                name="exang"
                value={formData.exang}
                onChange={handleChange}
                label="Exercise Induced Angina"
                required
              >
                <MenuItem value="0">No</MenuItem>
                <MenuItem value="1">Yes</MenuItem>
              </Select>
              {errors.exang && <FormHelperText>{errors.exang}</FormHelperText>}
            </FormControl>

            <FormControl fullWidth error={!!errors.slope}>
              <InputLabel>ST Slope</InputLabel>
              <Select
                name="slope"
                value={formData.slope}
                onChange={handleChange}
                label="ST Slope"
                required
              >
                <MenuItem value="0">Upsloping</MenuItem>
                <MenuItem value="1">Flat</MenuItem>
                <MenuItem value="2">Downsloping</MenuItem>
              </Select>
              {errors.slope && <FormHelperText>{errors.slope}</FormHelperText>}
            </FormControl>

            <FormControl fullWidth error={!!errors.ca}>
              <InputLabel>Number of Major Vessels</InputLabel>
              <Select
                name="ca"
                value={formData.ca}
                onChange={handleChange}
                label="Number of Major Vessels"
                required
              >
                <MenuItem value="0">0 vessels</MenuItem>
                <MenuItem value="1">1 vessel</MenuItem>
                <MenuItem value="2">2 vessels</MenuItem>
                <MenuItem value="3">3 vessels</MenuItem>
              </Select>
              {errors.ca && <FormHelperText>{errors.ca}</FormHelperText>}
            </FormControl>

            <FormControl fullWidth error={!!errors.thal}>
              <InputLabel>Thalassemia</InputLabel>
              <Select
                name="thal"
                value={formData.thal}
                onChange={handleChange}
                label="Thalassemia"
                required
              >
                <MenuItem value="0">Normal</MenuItem>
                <MenuItem value="1">Fixed Defect</MenuItem>
                <MenuItem value="2">Reversible Defect</MenuItem>
              </Select>
              {errors.thal && <FormHelperText>{errors.thal}</FormHelperText>}
            </FormControl>
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