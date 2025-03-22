import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
# Load preprocessed data
df = pd.read_csv("processed_data.csv")

# Feature selection
X = df.drop(columns=["lead_id", "converted"])
y = df["converted"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Feature Importance Analysis with SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test, check_additivity=False)

# Extract SHAP values for the positive class (converted = 1)
shap_values = shap_values[:, :, 1]  # Fix shape issue

# Final check
print("Fixed SHAP values shape:", shap_values.shape)
print("X_test shape:", X_test.shape)

shap.summary_plot(shap_values, X_test, show=False)
plt.savefig("shap_summary.png")

# Save model
pickle.dump(model, open("lead_model.pkl", "wb"))
print("Model training completed. Model saved as 'lead_model.pkl'.")
