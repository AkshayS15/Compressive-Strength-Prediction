import streamlit as st
from prediction_helper import predict_concrete_strength

# Streamlit UI
st.title("Concrete Strength Prediction")

# Create two columns
col1, col2 = st.columns(2)

# Collect inputs in two columns
with col1:
    cement = st.number_input("Cement (kg):", min_value=0.0)
    blast_furnace_slag = st.number_input("Blast Furnace Slag (kg):", min_value=0.0)
    fly_ash = st.number_input("Fly Ash (kg):", min_value=0.0)
    superplasticizer = st.number_input("Superplasticizer (kg):", min_value=0.0)

with col2:
    coarse_aggregate = st.number_input("Coarse Aggregate (kg):", min_value=0.0)
    fine_aggregate = st.number_input("Fine Aggregate (kg):", min_value=0.0)  # Removed the extra space
    age = st.number_input("Age (days):", min_value=0.0)
    water_cement_ratio = st.number_input("Water-Cement Ratio:", min_value=0.0)
    water = st.number_input("Water (kg):", min_value=0.0)

# Create a button to trigger prediction
if st.button("Predict"):
    input_data = {
        'cement': cement,
        'blast_furnace_slag': blast_furnace_slag,
        'fly_ash': fly_ash,
        'superplasticizer': superplasticizer,
        'coarse_aggregate': coarse_aggregate,
        'fine_aggregate': fine_aggregate,  # Updated here
        'age': age,
        'water_cement_ratio': water_cement_ratio,
        'water': water
    }

    # Call the prediction function
    prediction = predict_concrete_strength(input_data)
    st.success(f"Predicted Concrete Compressive Strength: {prediction:.2f} MPa")
