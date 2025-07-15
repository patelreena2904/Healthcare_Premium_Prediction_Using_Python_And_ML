import streamlit as st
import numpy as np
from prediction_helper import predict
# Title
st.title('Insurance Premium Prediction')


# Function to predict premium (Placeholder)
def predict_premium(inputs):
    # Placeholder for actual model prediction
    return np.random.randint(10000, 50000)  # Random prediction for illustration


# Create input fields in columns
st.write("### Please enter your details:")

# First Row: Age, Gender, Region
col1, col2, col3 = st.columns(3)
with col1:
    age = st.slider('Age', 18, 100, 30)
with col2:
    gender = st.selectbox('Gender', ['Male', 'Female'])
with col3:
    region = st.selectbox('Region', ['Northeast', 'Northwest', 'Southeast', 'Southwest'])

# Second Row: Marital Status, Dependants, BMI Category
col4, col5, col6 = st.columns(3)
with col4:
    marital_status = st.selectbox('Marital Status', ['Unmarried', 'Married'])
with col5:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, max_value=3, value=0)
with col6:
    bmi_category = st.selectbox('BMI Category', ['Overweight', 'Underweight', 'Normal', 'Obesity'])

# Third Row: Smoking Status, Employment Status, Income Level
col7, col8, col9 = st.columns(3)
with col7:
    smoking_status = st.selectbox('Smoking Status',
                                  ['Regular', 'No Smoking', 'Occasional', 'Smoking=0', 'Does Not Smoke', 'Not Smoking'])
with col8:
    employment_status = st.selectbox('Employment Status', ['Self-Employed', 'Freelancer', 'Salaried'])

# Fourth Row: Income Lakhs, Medical History, Insurance Plan
col10, col11, col12 = st.columns(3)
with col10:
    income_lakhs = st.number_input('Income (in Lakhs)', min_value=0, max_value=100, value=10)
with col11:
    medical_history = st.selectbox('Medical History', [
        'High blood pressure', 'No Disease', 'Diabetes & High blood pressure',
        'Diabetes & Heart disease', 'Diabetes', 'Diabetes & Thyroid',
        'Heart disease', 'Thyroid', 'High blood pressure & Heart disease'
    ])
with col12:
    insurance_plan = st.selectbox('Insurance Plan', ['Silver', 'Bronze', 'Gold'])

# Fifth Row: Genetical Risk
col13 = st.columns(1)
with col13[0]:
    genetical_risk = st.slider('Genetical Risk', 0, 5, 0)

# Predict Button

    # Gather input data
input_dict = {
        'age': age,
        'gender': gender,
        'region': region,
        'marital_status': marital_status,
        'number_of_dependants': number_of_dependants,
        'bmi_category': bmi_category,
        'smoking_status': smoking_status,
        'employment_status': employment_status,
        'income_lakhs': income_lakhs,
        'medical_history': medical_history,
        'insurance_plan': insurance_plan,
        'genetical_risk': genetical_risk
}
if st.button('Predict Annual Premium'):
    # Call the prediction function
    prediction=predict(input_dict)
    st.success(f"Predicted Premium:{prediction}")

