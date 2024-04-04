import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load("../Dataset/random_forest_model.joblib")

# Header Section
st.markdown(
    """
    <style>
        .header {
            background-color: #333;
            color: white;
            text-align: center;
            height: 60px;
            line-height: 60px;
            font-size: 24px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="header">Car Accident Severity Prediction</p>', unsafe_allow_html=True)
# Input fields for prediction
# Input fields for prediction
distance = st.number_input("Distance (mi)", min_value=0.0)
street = st.text_input("Street")
city = st.text_input("City")
county = st.text_input("County")
state = st.text_input("State")
zipcode = st.text_input("Zipcode")
country = st.text_input("Country")
timezone = st.text_input("Timezone")
wind_direction = st.selectbox("Wind Direction", options=["North", "South", "East", "West"])
weather_condition = st.text_input("Weather Condition")
amenity = st.checkbox("Amenity")
bump = st.checkbox("Bump")
crossing = st.checkbox("Crossing")
give_way = st.checkbox("Give Way")
junction = st.checkbox("Junction")
no_exit = st.checkbox("No Exit")
railway = st.checkbox("Railway")
roundabout = st.checkbox("Roundabout")
station = st.checkbox("Station")
stop = st.checkbox("Stop")
traffic_calming = st.checkbox("Traffic Calming")
traffic_signal = st.checkbox("Traffic Signal")
turning_loop = st.checkbox("Turning Loop")
sunrise_sunset = st.selectbox("Sunrise Sunset", options=["Sunrise", "Sunset"])
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")
submit_button = st.button("Submit Prediction")


    # Display the prediction result

# Dashboard Section
st.markdown(
    """
    <style>
        .dashboard {
            background-color: #f4f4f4;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: space-around;
        }
        .dashboard button {
            width: 25%;
            background-color: white;
            color: black;
            border: none;
            padding: 10px;
            cursor: pointer;
        }
        .dashboard button.active {
            background-color: #333;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    with st.markdown('<div class="dashboard">', unsafe_allow_html=True):
        prediction_button = st.button("Predictions", key="active")
        reports_button = st.button("Reports")
        settings_button = st.button("Settings")

        # Prediction Form Section
        st.markdown(
    """
    <style>
        .prediction-form {
            background-color: #f4f4f4;
            width: 50%;
            padding: 20px;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="prediction-form">', unsafe_allow_html=True)
# Add input fields for other columns similarly...

# Prediction Results Section
st.markdown(
"""
<style>
    .prediction-results {
        background-color: #f4f4f4;
        width: 50%;
        padding: 20px;
        margin-top: 20px;
    }
</style>
""",
unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="prediction-results">', unsafe_allow_html=True)
predicted_severity = st.text_input("Predicted Severity")
# Probability Distribution Chart
st.subheader("Probability Distribution")
# Key Features Visualization Chart
st.subheader("Key Features Visualization")

# Prediction History Section
st.markdown(
"""
<style>
    .prediction-history {
        background-color: #f4f4f4;
        width: 100%;
        padding: 20px;
        margin-top: 20px;
    }
</style>
""",
unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="prediction-history">', unsafe_allow_html=True)
st.subheader("Prediction History")
# Display Prediction History Table

# Reports Section
st.markdown(
"""
<style>
    .reports {
        background-color: #f4f4f4;
        width: 100%;
        padding: 20px;
        margin-top: 20px;
    }
</style>
""",
unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="reports">', unsafe_allow_html=True)
st.subheader("Reports")
# Severity Trends Over Time Chart
# Correlation between Features and Severity Chart
# Filter Options

# Settings Section
st.markdown(
"""
<style>
    .settings {
        background-color: #f4f4f4;
        width: 100%;
        padding: 20px;
        margin-top: 20px;
    }
</style>
""",
unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="settings">', unsafe_allow_html=True)
st.subheader("Settings")
# Model Configuration
# Update Machine Learning Model

# Footer Section
st.markdown(
"""
<style>
    .footer {
        background-color: #333;
        color: white;
        text-align: center;
        height: 60px;
        line-height: 60px;
        font-size: 14px;
    }
</style>
""",
unsafe_allow_html=True
)

st.markdown('<p class="footer">Contact Information | Privacy Policy | Terms of Service</p>', unsafe_allow_html=True)

# Predict function

# Create a LabelEncoder object
le = LabelEncoder()
from sklearn.preprocessing import LabelEncoder
# Create a LabelEncoder object
le = LabelEncoder()

# Fit the LabelEncoder on the training data for categorical columns
categorical_cols = ['Street', 'City', 'County', 'State', 'Zipcode', 'Country',
                    'Timezone', 'Wind_Direction', 'Weather_Condition', 'Sunrise_Sunset']
# Fit the LabelEncoder on categorical data
def predict_severity(Distance, Street, City, County, State, Zipcode, Country, Timezone, Wind_Direction, Weather_Condition, Amenity, Bump, Crossing, Give_Way, Junction, No_Exit, Railway, Roundabout, Station, Stop, Traffic_Calming, Traffic_Signal, Turning_Loop, Sunrise_Sunset, Start_Date, End_Date, Start_Time, End_Time):
    # Fit the LabelEncoder on the categorical data
    le.fit([Street, City, County, State, Zipcode, Country, Timezone, Wind_Direction,
            Weather_Condition, Sunrise_Sunset])
#Start_Date, End_Date, Start_Time, End_Time
    # Encode categorical variables
    street_encoded = le.transform([Street])
    city_encoded = le.transform([City])
    county_encoded = le.transform([County])
    state_encoded = le.transform([State])
    zipcode_encoded = le.transform([Zipcode])
    country_encoded = le.transform([Country])
    timezone_encoded = le.transform([Timezone])
    wind_direction_encoded = le.transform([Wind_Direction])
    weather_condition_encoded = le.transform([Weather_Condition])
    sunrise_sunset_encoded = le.transform([Sunrise_Sunset])
    #start_date_encoded = le.transform([Start_Date])
    #end_date_encoded = le.transform([End_Date])
    #start_time_encoded = le.transform([Start_Time])
    #end_time_encoded = le.transform([End_Time])

    # Process input data
    input_data = pd.DataFrame({
        "Distance(mi)": [Distance],
        "Street": street_encoded,
        "City": city_encoded,
        "County": county_encoded,
        "State": state_encoded,
        "Zipcode": zipcode_encoded,
        "Country": country_encoded,
        "Timezone": timezone_encoded,
        "Wind_Direction": wind_direction_encoded,
        "Weather_Condition": weather_condition_encoded,
        "Amenity": [Amenity],
        "Bump": [Bump],
        "Crossing": [Crossing],
        "Give_Way": [Give_Way],
        "Junction": [Junction],
        "No_Exit": [No_Exit],
        "Railway": [Railway],
        "Roundabout": [Roundabout],
        "Station": [Station],
        "Stop": [Stop],
        "Traffic_Calming": [Traffic_Calming],
        "Traffic_Signal": [Traffic_Signal],
        "Turning_Loop": [Turning_Loop],
        "Sunrise_Sunset": sunrise_sunset_encoded,
        "Start_Date": [Start_Date],
        "End_Date": [End_Date],
        "Start_Time": [Start_Time],
        "End_Time": [End_Time]
    })

    # Make prediction using the model
    prediction = model.predict(input_data)

    return prediction

# Check if the submit button is clicked
if submit_button:
    # Call the predict_severity function with user inputs
    prediction = predict_severity(
        distance, street, city, county, state, zipcode, country, timezone, wind_direction,
        weather_condition, amenity, bump, crossing, give_way, junction, no_exit, railway,
        roundabout, station, stop, traffic_calming, traffic_signal, turning_loop, sunrise_sunset,
        start_date, end_date, start_time, end_time
    )
    st.write("Predicted Severity:", prediction)