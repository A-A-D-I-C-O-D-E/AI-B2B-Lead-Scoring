import streamlit as st
import requests
import os
from voice import text_to_speech  # Import voice function

# Title
st.title("📊 AI Lead Scoring Dashboard")

# Sidebar Inputs
st.sidebar.header("Enter Lead Data")

# Get user input
website_visits = st.sidebar.number_input("Website Visits", min_value=0, step=1)
email_opens = st.sidebar.number_input("Email Opens", min_value=0, step=1)
demo_requests = st.sidebar.number_input("Demo Requests", min_value=0, step=1)
sales_calls = st.sidebar.number_input("Sales Calls", min_value=0, step=1)
annual_revenue = st.sidebar.number_input("Annual Revenue", min_value=0.0, step=1000.0)
conversion_probability = st.sidebar.slider("Conversion Probability", 0.0, 1.0, 0.5)

# Dropdown for categorical values
company_size = st.sidebar.selectbox("Company Size", ["Small", "Medium", "Large"])
industry = st.sidebar.selectbox("Industry", ["Tech", "Finance", "Healthcare", "Retail", "Other"])

# Predict Button
if st.sidebar.button("🔮 Predict Lead Score"):
    lead_data = {
        "website_visits": website_visits,
        "email_opens": email_opens,
        "demo_requests": demo_requests,
        "sales_calls": sales_calls,
        "annual_revenue": annual_revenue,
        "conversion_probability": conversion_probability,
        "company_size": company_size,
        "industry": industry,
    }

    # API URL
    api_url = "http://127.0.0.1:8000/predict"

    try:
        response = requests.post(api_url, json=lead_data)

        if response.status_code == 200:
            result = response.json()
            lead_score = result['lead_score']
            st.success(f"🎯 Predicted Lead Score: {lead_score:.2f}")

            # Generate voice feedback
            audio_file = text_to_speech(f"The predicted lead score is {lead_score:.2f}")

            # Check if audio file was created successfully
            if audio_file and os.path.exists(audio_file):
                st.audio(audio_file, format="audio/mp3")
            else:
                st.error("❌ Speech generation failed.")

        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("⚠️ API Server is not running. Please start the FastAPI server.")
