from flask import Flask, render_template, request
from heart_disease_model import predict_heart_disease

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            features = [
                int(request.form["age"]),
                int(request.form["sex"]),
                int(request.form["chest_pain_type"]),
                int(request.form["resting_blood_pressure"]),
                int(request.form["cholesterol"]),
                int(request.form["fasting_blood_sugar"]),
                int(request.form["resting_electrocardiographic_results"]),
                int(request.form["max_heart_rate_achieved"]),
                int(request.form["exercise_induced_angina"]),
                float(request.form["st_depression"]),
                int(request.form["st_slope"]),
                int(request.form["number_of_major_vessels"]),
                int(request.form["thalassemia"])
            ]
            
            prediction = predict_heart_disease(features)
            result = "The model predicts heart disease." if prediction == 1 else "The model predicts no heart disease."
            return render_template("index.html", result=result)
        
        except ValueError as e:
            error = f"Invalid input: {str(e)}"
        except Exception as e:
            error = f"An error occurred: {str(e)}"
        return render_template("index.html", result=error)
    
    return render_template("index.html")