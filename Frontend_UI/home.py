import streamlit as st
from prediction_results import display_probability_distribution
from prediction_form import display_prediction_form
from prediction_history import display_prediction_history
from reports import display_reports

def display_home():
    # Set page layout
    col1, col2 = st.columns([1, 2])  # Adjust the column ratios as needed

    # Prediction Form
    with col1:
        prediction = display_prediction_form()
    with col2:
        probabilities = [0.1, 0.2, 0.3, 0.4]  # Example probabilities
        display_probability_distribution(probabilities)
        prediction_history = [
            ['2021-01-01 10:00 AM', 'City 1', 'High', 'High', 'Correct'],
            ['2021-01-02 02:00 PM', 'City 2', 'Low', 'Medium', 'Incorrect'],
            ['2021-01-03 05:00 PM', 'City 3', 'Medium', 'Medium', 'Correct']
        ]
        display_prediction_history(prediction_history)
        if (prediction) in [1,2,3,4]:
            st.write("Predicted Severity Level:")
            st.write(prediction)
    display_reports()