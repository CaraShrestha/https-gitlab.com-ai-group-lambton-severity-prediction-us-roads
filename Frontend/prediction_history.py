import streamlit as st
import pandas as pd

def display_prediction_history(prediction_history):
    df = pd.DataFrame(prediction_history, columns=['Date and Time', 'Location', 'Actual Severity', 'Predicted Severity', 'Outcome'])
    st.markdown('## Prediction History')  # Larger header for prediction history    # Use CSS to adjust table width
    st.write(
        f"""
        <style>
            .reportview-container .main .block-container{{max-width: 100%;}}
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Display prediction history table
    st.table(df)
