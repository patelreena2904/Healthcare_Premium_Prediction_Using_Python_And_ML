
# ML-healthcare_premium-Prediction-Regression

## Project Overview

This project involves predicting health care premiums based on various features using machine learning regression techniques. The goal is to develop a model that can accurately predict the annual premium amount a person should pay, based on their demographic and health-related information.

## Features

- **Data Preprocessing**: Handles categorical variables, encodes insurance plans, and processes medical history. Medical history is split into diseases, and risk scores are assigned accordingly.
- **Normalization**: Risk scores are normalized to ensure consistent scaling.
- **Scaling**: Data is scaled based on age using different scalers for individuals `<= 25` years and those `> 25` years.
- **Regression Models**: Implements and evaluates various regression models to predict the annual premium amount.
- **Streamlit Application**: Provides an interactive interface for users to input their data and receive predictions.

## Data Columns

- **age**: Age of the individual.
- **gender**: Gender of the individual (Male, Female).
- **region**: Geographic region (Northeast, Northwest, Southeast, Southwest).
- **marital_status**: Marital status (Unmarried, Married).
- **number_of_dependants**: Number of dependents.
- **bmi_category**: Body Mass Index category (Overweight, Underweight, Normal, Obesity).
- **smoking_status**: Smoking status (Regular, No Smoking, Occasional, Smoking=0, Does Not Smoke, Not Smoking).
- **employment_status**: Employment status (Self-Employed, Freelancer, Salaried).
- **income_level**: Income level categorized as per income brackets (> 40L, <10L, 10L - 25L, 25L - 40L).
- **income_lakhs**: Actual income in lakhs.
- **medical_history**: Medical history including various diseases (e.g., Diabetes, High blood pressure).
- **insurance_plan**: Type of insurance plan (Bronze, Silver, Gold).
- **annual_premium_amount**: Target variable - the annual premium amount to be predicted.
- **genetical_risk**: Genetical risk score.

## Data Preprocessing Function

The preprocessing function handles the following:

1. **Medical History**: Splits medical history into diseases, converts to lowercase, and maps to risk scores.
2. **Normalization**: Normalizes risk scores to ensure all values are on a comparable scale.

## Scaling Function

The scaling function applies different scalers based on age:

- **scaler_young.joblib**: Applied if age `<= 25`.
- **scaler_rest.joblib**: Applied if age `> 25`.

## Machine Learning Models

The project trains and evaluates various regression models, including:

- Linear Regression
- Random Forest Regressor
- Other models as needed

Model performance is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

## Streamlit Application

A Streamlit application is developed to provide an interactive interface for:

- Inputting personal and health-related information.
- Receiving predictions for the annual premium amount based on the inputs.

## File Structure

- `data/`: Contains datasets used for training and testing.
- `src/`: Contains Python scripts for data preprocessing, model training, and evaluation.
- `app/`: Contains the Streamlit application files.
- `models/`: Contains saved models and scalers.
- `notebooks/`: Contains Jupyter notebooks for exploratory data analysis and model prototyping.
- `requirements.txt`: Lists the Python packages required for the project.
- `README.md`: This file.

