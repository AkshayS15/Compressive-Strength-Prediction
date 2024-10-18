import numpy as np
import joblib
import os
import streamlit as st

# Define the paths
scaler_path = os.path.join('artifacts', 'scaler.joblib')
model_path = os.path.join('artifacts', 'ml_model.joblib')

# Load the scaler and model
try:
    scaler_with_cols = joblib.load(scaler_path)
    model = joblib.load(model_path)
    scaler = scaler_with_cols['scaler']
    cols_to_scale = scaler_with_cols['cols_to_scale']
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}")


# Define the prediction function
def predict_concrete_strength(input_data):
    # Validate input data
    for col in cols_to_scaler:
        if col not in input_data:
            raise ValueError(f"Missing input data for column: {col}")

    # Convert input_data dict to a numpy array (ensure order matches training)
    input_array = np.array([input_data[col] for col in cols_to_scale])

    # Scale the input data
    scaled_input = scaler.transform([input_array])

    # If water column exists in cols_to_scale, drop it after scaling
    if 'water' in cols_to_scale:
        water_index = cols_to_scale.index('water')
        scaled_input = np.delete(scaled_input, water_index, axis=1)  # Remove water column

    # Make prediction using the model
    prediction = model.predict(scaled_input)

    return prediction[0]  # Return the predicted concrete strength
