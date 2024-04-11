import streamlit as st
from reports import display_reports
from prediction_form import display_prediction_form
from prediction_history import display_prediction_history

from home import display_home

st.set_page_config(layout="wide")
# Add a sidebar for navigation
menu = ["Home","Reports", "Settings", "Prediction form"]
choice = st.sidebar.radio("Navigation", menu)

# Display selected page content based on user choice
if choice == "Home":
    display_home()
elif choice == "Reports":
    display_reports()

elif choice == "Prediction form":
    display_prediction_form()
