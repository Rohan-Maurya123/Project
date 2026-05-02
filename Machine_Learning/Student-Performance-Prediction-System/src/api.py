from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI(title="Student Performance Prediction API")

# Load artifacts
try:
    model = joblib.load(os.path.join('models', 'student_model.pkl'))
    scaler = joblib.load(os.path.join('models', 'scaler.pkl'))
    feature_names = joblib.load(os.path.join('models', 'feature_names.pkl'))
    label_mappings = joblib.load(os.path.join('models', 'label_mappings.pkl'))
except Exception as e:
    print(f"Error loading models: {e}")

class StudentData(BaseModel):
    school: str
    sex: str
    age: int
    address: str
    famsize: str
    Pstatus: str
    Medu: int
    Fedu: int
    Mjob: str
    Fjob: str
    reason: str
    guardian: str
    traveltime: int
    studytime: int
    failures: int
    schoolsup: str
    famsup: str
    paid: str
    activities: str
    nursery: str
    higher: str
    internet: str
    romantic: str
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Performance Prediction API"}

@app.post("/predict")
def predict(data: StudentData):
    try:
        # Convert input to DataFrame
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])
        
        # Apply label encoding using the saved mappings
        for col, mapping in label_mappings.items():
            if col in input_df.columns:
                # Handle unseen values by defaulting to a known value or raising error
                val = input_df[col].iloc[0]
                if val in mapping:
                    input_df[col] = mapping[val]
                else:
                    # Fallback to the first available category if unknown
                    input_df[col] = list(mapping.values())[0]
        
        # Ensure column order matches training
        input_df = input_df[feature_names]
        
        # Scale
        input_scaled = scaler.transform(input_df)
        
        # Predict
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)[0]
        
        result = "Pass" if prediction[0] == 1 else "Fail"
        confidence = float(probability[1]) if prediction[0] == 1 else float(probability[0])
        
        return {
            "prediction": result,
            "confidence": round(confidence, 4),
            "status": "Success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
