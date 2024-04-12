import streamlit as st
from prediction_results import display_probability_distribution
from prediction_form import display_prediction_form,save_prediction_to_history
from prediction_history import display_prediction_history
from reports_page import display_reports
import pandas as pd
def display_home():
    df_encoded = pd.DataFrame()
    prediction = None  # Initialize prediction to None
    # Set page layout
    col1, col2 = st.columns([1, 2])  # Adjust the column ratios as needed
    # Prediction Form
    with col1:
        result = display_prediction_form()
        if result is not None:
            prediction, df_encoded = result
        else:
            # Handle the case when display_prediction_form() returns None
            st.write("Prediction form returned None")
    with col2:
        probabilities = [0.1, 0.2, 0.3, 0.4]  # Example probabilities
        display_probability_distribution(probabilities)
        if not df_encoded.empty:
            save_prediction_to_history(df_encoded, prediction)
            display_prediction_history()
        if (prediction) in [1,2,3,4]:
            st.write("Predicted Severity Level:")
            st.write(prediction)
    display_reports()