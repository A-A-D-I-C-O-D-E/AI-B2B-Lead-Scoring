from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

# Load trained model
model = pickle.load(open("lead_model.pkl", "rb"))

# Load dataset to fit encoders
df = pd.read_csv("processed_data.csv")

# Encode categorical variables
label_enc = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
label_enc.fit(df[["company_size", "industry"]])

# Load scaler if the model was trained with scaled data
try:
    scaler = pickle.load(open("scaler.pkl", "rb"))
    scaling_enabled = True
except FileNotFoundError:
    scaling_enabled = False

app = FastAPI()

class LeadInput(BaseModel):
    website_visits: int
    email_opens: int
    demo_requests: int
    sales_calls: int
    annual_revenue: float
    conversion_probability: float
    company_size: str
    industry: str

    @field_validator("annual_revenue")
    @classmethod
    def check_annual_revenue(cls, v):
        if v < 0:
            raise ValueError("Annual revenue cannot be negative.")
        return v

    @field_validator("conversion_probability")
    @classmethod
    def check_conversion_probability(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Conversion probability must be between 0 and 1.")
        return v

@app.get("/")
def home():
    return {"message": "Lead scoring API is running!"}

@app.post("/predict")
def predict(lead: LeadInput):
    try:
        # Handle unknown categorical values
        if lead.company_size not in label_enc.categories_[0]:
            lead.company_size = df["company_size"].mode()[0]  # Assign most frequent value
        
        if lead.industry not in label_enc.categories_[1]:
            lead.industry = df["industry"].mode()[0]  # Assign most frequent value
        
        # Encode categorical features
        encoded_values = label_enc.transform([[lead.company_size, lead.industry]])[0]

        # Prepare input features
        features = np.array([[   
            lead.website_visits, lead.email_opens, lead.demo_requests,
            lead.sales_calls, lead.annual_revenue, lead.conversion_probability,
            encoded_values[0], encoded_values[1]
        ]])

        # Apply scaling if the model was trained with scaled data
        if scaling_enabled:
            features = scaler.transform(features)

        # Debugging: Print inputs before making predictions
        print("Final Features for Prediction:", features)

        # Ensure shape consistency
        if hasattr(model, "n_features_in_") and features.shape[1] != model.n_features_in_:
            raise HTTPException(status_code=400, detail="Feature mismatch with model")

        # Predict lead score
        score = model.predict_proba(features)[0][1]
        return {"lead_score": round(score, 4)}  # Rounded for better readability
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
