import numpy as np
import joblib

# Load the saved scaler and model
scaler_with_cols = joblib.load("artifacts/scaler.joblib")  # Adjust path as needed
model = joblib.load("artifacts/ml_model.joblib")  # Adjust path as needed

# Extract the scaler and the columns used for scaling
scaler = scaler_with_cols['scaler']  # The MinMaxScaler object
cols_to_scale = scaler_with_cols['cols_to_scale']  # List of columns that were scaled


# Define the prediction function
def predict_concrete_strength(input_data):
    # Validate input data
    for col in cols_to_scale:
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
