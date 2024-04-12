import streamlit as st
import pandas as pd
import joblib
import os
# Define the path to the prediction history CSV file
PREDICTION_HISTORY_FILE = '../History/prediction_history.csv'
# Preprocessing function for one-hot encoding categorical variables
def choose_model(option):
    random_forest_estimator_5 = joblib.load('../Dataset/random_forest_model_dump.joblib')
    random_forest_model_estimator_15 = joblib.load('../Dataset/random_forest_model.joblib')
    if option=="Random Forest Estimator 5":
        return random_forest_estimator_5
    else:
        return random_forest_model_estimator_15
def preprocess_input(df):
    # Define all categorical columns used during training
    categorical_cols = ['Street', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone','Start_Date','End_Date'
                        ,'Wind_Direction', 'Weather_Condition', 'Sunrise_Sunset','Start_Time','End_Time']

    # Check if 'Sunrise_Sunset' column exists in the DataFrame
    if 'Sunrise_Sunset' in df.columns:
        # One-hot encode categorical variables
        df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    else:
        # If 'Sunrise_Sunset' column is not present, create an empty DataFrame with all categorical columns
        df_encoded = pd.DataFrame(columns=categorical_cols)
    # Ensure all columns present in the training data are also present in the input data
    # Replace these columns with the actual columns used during model training
    expected_columns = ['Distance(mi)', 'Street', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone',
                        'Wind_Direction', 'Weather_Condition', 'Amenity', 'Bump', 'Crossing', 'Give_Way',
                        'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming',
                        'Traffic_Signal', 'Turning_Loop', 'Sunrise_Sunset', 'Start_Date', 'End_Date',
                        'Start_Time', 'End_Time']

    for col in expected_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    # Reorder columns to match the order in the training data
    df_encoded = df_encoded[expected_columns]

    return df_encoded

def save_prediction_to_history(data, prediction):
    # Create or append to the prediction history CSV file
    if not os.path.exists(PREDICTION_HISTORY_FILE):
        df = pd.DataFrame(columns=['Date and Time', 'Location', 'Actual Severity', 'Predicted Severity'])
        df.to_csv(PREDICTION_HISTORY_FILE, index=False)
    # Append the new prediction(s) to the CSV file
    columns_to_select = ['Start_Date', 'End_Date']  # Specify the columns to select
    selected_columns = [data[col].iloc[0] for col in columns_to_select]  # Select the specified columns
    selected_columns.append(prediction)  # Append the prediction column
    if len(selected_columns) == 3:  # Ensure the correct number of columns
        with open(PREDICTION_HISTORY_FILE, 'a') as file:
            file.write(','.join(map(str, selected_columns)) + '\n')
    else:
        print("Error: Incorrect number of columns selected.")


def display_prediction_form():
    # Prediction Form
    st.header("Severity Prediction Form")

    # Input fields for each feature
    col1, col2 = st.columns(2)

    with col1:
        street = st.text_input("Street")
        state = st.text_input("State")
        zipcode = st.text_input("Zipcode")
        county = st.text_input("County")
        weather_condition = st.text_input("Weather Condition")
        bump = st.checkbox("Bump")
        give_way = st.checkbox("Give Way")
        no_exit = st.checkbox("No Exit")
        roundabout = st.checkbox("Roundabout")
        stop = st.checkbox("Stop")
        traffic_signal = st.checkbox("Traffic Signal")
        traffic_calming = st.checkbox("Traffic Calming")
    with col2:
        city = st.text_input("City")
        country = st.text_input("Country")
        timezone = st.text_input("Timezone")
        wind_direction = st.text_input("Wind Direction")
        sunrise_sunset = st.selectbox("Sunrise Sunset", ['Day', 'Night'])
        amenity = st.checkbox("Amenity")
        crossing = st.checkbox("Crossing")
        junction = st.checkbox("Junction")
        railway = st.checkbox("Railway")
        station = st.checkbox("Station")
        turning_loop = st.checkbox("Turning Loop")

    col1,col2 = st.columns(2)
    with col1:
        start_date = st.text_input("Start Date YYYY-MM-DD")
        start_time = st.text_input("Start Time HH:MM:SS")

    with col2:
        end_date = st.text_input("End Date YYYY-MM-DD")
        end_time = st.text_input("End Time HH:MM:SS")

    distance = st.number_input("Distance (mi)")
    sunrise_sunset_numeric = 1 if sunrise_sunset == 'Day' else 0
    option=st.selectbox("Machine Learning Model",['Random Forest Estimator 5','Random Forest Estimator 15'])

    # Submit button
    if st.button("Submit"):
        # Create a DataFrame from the input values
        data = {
            'Distance(mi)': [distance],
            'Street': [street],
            'City': [city],
            'County': [county],
            'State': [state],
            'Zipcode': [zipcode],
            'Country': [country],
            'Timezone': [timezone],
            'Wind_Direction': [wind_direction],
            'Weather_Condition': [weather_condition],
            'Amenity': [1 if amenity else 0],
            'Bump': [1 if bump else 0],
            'Crossing': [1 if crossing else 0],
            'Give_Way': [1 if give_way else 0],
            'Junction': [1 if junction else 0],
            'No_Exit': [1 if no_exit else 0],
            'Railway': [1 if railway else 0],
            'Roundabout': [1 if roundabout else 0],
            'Station': [1 if station else 0],
            'Stop': [1 if stop else 0],
            'Traffic_Calming': [1 if traffic_calming else 0],
            'Traffic_Signal': [1 if traffic_signal else 0],
            'Turning_Loop': [1 if turning_loop else 0],
            'Sunrise_Sunset': [sunrise_sunset_numeric],
            'Start_Date': [start_date],
            'End_Date': [end_date],
            'Start_Time': [start_time],
            'End_Time': [end_time]
        }

        # # Define the data as a dictionary
        # data2 = {
        #     "Distance(mi)": [0.0],
        #     "Street": ["Pennsylvania Avenue"],
        #     "City": [""],
        #     "County": [""],
        #     "State": [""],
        #     "Zipcode": [""],
        #     "Country": [""],
        #     "Timezone": [""],
        #     "Wind_Direction": [""],
        #     "Weather_Condition": [""],
        #     "Amenity": [0],
        #     "Bump": [0],
        #     "Crossing": [0],
        #     "Give_Way": [0],
        #     "Junction": [0],
        #     "No_Exit": [0],
        #     "Railway": [0],
        #     "Roundabout": [0],
        #     "Station": [0],
        #     "Stop": [0],
        #     "Traffic_Calming": [0],
        #     "Traffic_Signal": [0],
        #     "Turning_Loop": [1],
        #     "Sunrise_Sunset": [1],
        #     "Start_Date": ["2020-10-10"],
        #     "End_Date": ["2020-10-13"],
        #     "Start_Time": ["10:30"],
        #     "End_Time": ["10:40"]
        # }
        # Display the DataFrame
        df = pd.DataFrame(data)
        df_encoded = preprocess_input(df)
        # Make predictions
        model= choose_model(option)
        predictions = model.predict(df_encoded)
        return predictions[0], df  # Returning both predictions[0] and df_encoded