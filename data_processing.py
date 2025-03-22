import pandas as pd
import pickle
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler

# Load dataset
df = pd.read_csv("b2b_lead_scoring_dataset.csv")

# Handle missing values (replace NaNs)
df.fillna(method='ffill', inplace=True)

# Encode categorical features properly
ordinal_enc = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
df[["company_size", "industry"]] = ordinal_enc.fit_transform(df[["company_size", "industry"]])

# Scale numerical features
scaler = MinMaxScaler()
num_features = ["website_visits", "email_opens", "demo_requests", "sales_calls", "annual_revenue", "conversion_probability"]
df[num_features] = scaler.fit_transform(df[num_features])

# Save processed data
df.to_csv("processed_data.csv", index=False)
print("Data preprocessing completed. Processed data saved as 'processed_data.csv'.", flush=True)

