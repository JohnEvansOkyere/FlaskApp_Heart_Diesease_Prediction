from pydantic import BaseModel, Field
from typing import Optional

class HeartDiseaseInput(BaseModel):
    age: int = Field(..., ge=0, le=120, description="Age in years")
    sex: int = Field(..., ge=0, le=1, description="Sex (1 = male, 0 = female)")
    chest_pain_type: int = Field(..., ge=0, le=3, description="Chest pain type (0-3)")
    resting_blood_pressure: int = Field(..., ge=0, le=300, description="Resting blood pressure in mm Hg")
    cholesterol: int = Field(..., ge=0, le=600, description="Serum cholesterol in mg/dl")
    fasting_blood_sugar: int = Field(..., ge=0, le=1, description="Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)")
    resting_ecg: int = Field(..., ge=0, le=2, description="Resting ECG results (0-2)")
    max_heart_rate: int = Field(..., ge=0, le=300, description="Maximum heart rate achieved")
    exercise_angina: int = Field(..., ge=0, le=1, description="Exercise induced angina (1 = yes, 0 = no)")
    st_depression: float = Field(..., ge=0.0, le=10.0, description="ST depression induced by exercise relative to rest")
    st_slope: int = Field(..., ge=0, le=2, description="Slope of the peak exercise ST segment (0-2)")
    number_of_vessels: int = Field(..., ge=0, le=3, description="Number of major vessels colored by fluoroscopy (0-3)")
    thalassemia: int = Field(..., ge=0, le=2, description="Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)")

class HeartDiseaseResponse(BaseModel):
    prediction: int = Field(..., description="Prediction (1 = high risk, 0 = low risk)")
    probability: float = Field(..., ge=0.0, le=1.0, description="Probability of heart disease")
    message: str = Field(..., description="Human-readable prediction message") 