from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models.schemas import HeartDiseaseInput, HeartDiseaseResponse
from .models.predictor import HeartDiseasePredictor
import pandas as pd

app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease risk using machine learning",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "https://flask-app-heart-diesease-prediction.vercel.app"  # your Vercel frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize the predictor
predictor = HeartDiseasePredictor()

@app.get("/")
async def root():
    return {"message": "Welcome to the Heart Disease Prediction API"}

@app.post("/api/predict", response_model=HeartDiseaseResponse)
async def predict(input_data: HeartDiseaseInput):
    try:
        # Convert input data to list of features
        features = [
            input_data.age,
            input_data.sex,
            input_data.chest_pain_type,
            input_data.resting_blood_pressure,
            input_data.cholesterol,
            input_data.fasting_blood_sugar,
            input_data.resting_ecg,
            input_data.max_heart_rate,
            input_data.exercise_angina,
            input_data.st_depression,
            input_data.st_slope,
            input_data.number_of_vessels,
            input_data.thalassemia
        ]
        
        # Make prediction
        prediction = predictor.predict(features)
        probability = predictor.get_prediction_probability(features)
        
        return HeartDiseaseResponse(
            prediction=prediction,
            probability=probability,
            message="High risk of heart disease" if prediction == 1 else "Low risk of heart disease"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#data = pd.read_csv("backend/data/heart.csv") 