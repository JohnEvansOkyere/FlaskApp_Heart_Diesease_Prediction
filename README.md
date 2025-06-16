# Heart Disease Prediction System

A modern web application for predicting heart disease risk using machine learning. The system uses a Random Forest Classifier trained on the UCI Heart Disease dataset.

## Features

- Modern React frontend with Material-UI components
- Flask backend with RESTful API
- Machine learning model for heart disease prediction
- Real-time prediction with probability scores
- Responsive design for all devices
- Input validation and error handling

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   └── utils/
│   ├── data/
│   └── models/
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       └── services/
└── README.md
```

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

## Installation

### Backend Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Running the Application

### Backend

1. Start the Flask server:
   ```bash
   cd backend
   python run.py
   ```
   The server will run on http://localhost:5000

### Frontend

1. Start the React development server:
   ```bash
   cd frontend
   npm start
   ```
   The application will open in your browser at http://localhost:3000

## API Endpoints

### POST /api/predict

Predicts heart disease risk based on input features.

Request body:
```json
{
  "age": 63,
  "sex": 1,
  "chest_pain_type": 3,
  "resting_blood_pressure": 145,
  "cholesterol": 233,
  "fasting_blood_sugar": 1,
  "resting_ecg": 0,
  "max_heart_rate": 150,
  "exercise_angina": 0,
  "st_depression": 2.3,
  "st_slope": 0,
  "number_of_vessels": 0,
  "thalassemia": 1
}
```

Response:
```json
{
  "prediction": 1,
  "probability": 0.85,
  "message": "High risk of heart disease"
}
```

## Model Information

The system uses a Random Forest Classifier with the following parameters:
- n_estimators: 500
- criterion: entropy
- max_depth: 8
- min_samples_split: 5

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 