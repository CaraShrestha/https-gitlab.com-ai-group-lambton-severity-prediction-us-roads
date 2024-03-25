# Severity Prediction US Roads

Our project aims to develop a predictive model for accident severity, utilizing machine learning algorithms within a Streamlit frontend and Flask deployment. By integrating data analysis, machine learning, frontend development with Streamlit, and deployment with Flask, we seek to provide insurance companies with valuable insights for risk assessment and premium determination. Users will interact with the user-friendly Streamlit frontend to input data and receive predictions, while the Flask backend manages model inference and serves prediction results over the web. Ultimately, our project endeavors to contribute to safer roads and more efficient insurance practices by delivering actionable insights to insurance companies, aiding them in understanding and mitigating the risks associated with accidents.


## Dataset Setup

1. **Copy Dataset File**: 
   - Place your dataset file(s) from this location https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents inside the `Dataset` folder in the project directory.

2. **Specify Dataset Path**:
   - Open `Utilities/constants.py`.
   - Locate the `DATASET_PATH` variable.
   - Set `DATASET_PATH` to the relative path of your dataset file within the `Dataset` folder. For example:
     ```python
     DATASET_PATH = 'Dataset/your_dataset_file.csv'
     ```

## Gitignore and Excluded Files

This project utilizes a `.gitignore` file to exclude certain files and folders from version control. Here are the contents of the `.gitignore` file:

## Install the required pacakges listed in requirements.txt
Install all the packages listed in requirements.txt using `pip install -r requirements.txt` and run the project

You are good to go!