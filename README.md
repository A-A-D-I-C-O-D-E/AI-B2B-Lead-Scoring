# 🚀 AI-Powered B2B Lead Scoring System  
An AI-driven sales assistant designed to help B2B logistics companies prioritize high-value leads efficiently. This system leverages **machine learning, a REST API, an interactive dashboard, and voice AI** to streamline lead qualification.

## 🔥 Key Features  
### 1️⃣ Lead Scoring & Insights  
✅ Predicts lead conversion probability using a trained ML model  
✅ Provides key insights using **SHAP values** to explain lead importance  

### 2️⃣ Seamless Integration  
✅ **REST API (FastAPI)** – Easily integrates with existing CRMs  
✅ **Streamlit Dashboard** – User-friendly interface for lead visualization  

### 3️⃣ AI-Enhanced Interaction  
✅ **Voice AI** – Reads predictions aloud for a real AI employee feel  
✅ **Human Feedback Loop** – Learns from user input to refine predictions over time  

---

## 🛠️ Installation & Setup  
Follow these steps to set up and run the project locally.  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/A-A-D-I-C-O-D-E/AI-B2B-Lead-Scoring.git
cd AI-B2B-Lead-Scoring
```

### 2️⃣ Install Dependencies  
Ensure **Python 3.8+** is installed, then run:  
```sh
pip install -r requirements.txt
```

### 3️⃣ Start the API Server (FastAPI)  
```sh
uvicorn api.main:app --reload
```
💡 API Available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
🔗 Interactive API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

### 4️⃣ Launch the Streamlit Dashboard  
```sh
streamlit run dashboard/dashboard.py
```
✅ Opens a web-based UI to input lead data and get predictions.  

---

## 🎯 How to Use the AI  
### 1️⃣ API Usage – Predict Lead Score  
Send a **POST request** with lead details:  

#### 🔹 API Request  
```json
{
  "website_visits": 15,
  "email_opens": 5,
  "demo_requests": 2,
  "sales_calls": 3,
  "annual_revenue": 500000,
  "conversion_probability": 0.7,
  "company_size": "Medium",
  "industry": "Tech"
}
```

#### 🔹 API Response  
```json
{
  "lead_score": 0.57
}
```
💡 **Higher lead scores indicate stronger conversion potential!**  

### 2️⃣ Streamlit Dashboard  
✅ **Manually input lead data** and visualize scores  
✅ **Feature importance** – Understand which factors matter most  
✅ **Voice AI** – Speaks out predictions  
✅ **User Feedback Loop** – Helps refine future predictions  

---

## 🔊 Voice AI Integration  
The system supports **Eleven Labs** or **Google TTS** for voice output.  
💡 If speech isn’t working:  
- Ensure a **stable internet connection** (for API-based TTS)  
- Verify that the **TTS API key** is correctly configured  

---

## 🚀 Future Enhancements  
🔹 **Cloud Deployment** – Deploy to AWS/GCP for real-time CRM integration  
🔹 **Enhanced Model Accuracy** – Improve data preprocessing and feature engineering  
🔹 **Multi-Language Support** – Expand for global sales teams  

This AI assistant **continuously learns and evolves**, making lead qualification **smarter and more efficient** over time! 🚀
