import streamlit as st
import pandas as pd
import os
import base64
# Define the path to the prediction history CSV file
PREDICTION_HISTORY_FILE = '../History/prediction_history.csv'

def display_prediction_history():
    # Load prediction history from the CSV file
    if os.path.exists(PREDICTION_HISTORY_FILE):
        prediction_history = pd.read_csv(PREDICTION_HISTORY_FILE)
        st.markdown('## Prediction History')  # Larger header for prediction history

        # Define custom CSS styles for the table
        custom_css = """
            <style>
            .custom-table {
                width: 100%; /* Set table width to 100% */
                border-collapse: collapse;
                border-spacing: 0;
                margin-bottom: 16px;
            }
            .custom-table th,
            .custom-table td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #e0e0e0;
            }
            .custom-table th {
                background-color: #f2f2f2;
                font-weight: bold;
            }
            </style>
        """
        st.write(custom_css, unsafe_allow_html=True)
        # Display prediction history table using st.table
        st.table(prediction_history)

        # Add download button using st.button
        if st.button("Download Prediction History CSV File"):
            csv = prediction_history.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # Convert DataFrame to bytes
            href = f'<a href="data:file/csv;base64,{b64}" download="prediction_history.csv">Download Prediction History</a>'
            st.markdown(href, unsafe_allow_html=True)
    else:
        st.write("No prediction history available.")
