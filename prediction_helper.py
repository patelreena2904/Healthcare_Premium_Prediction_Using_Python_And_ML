import pandas as pd
from joblib import load
model_rest=load("artifacts/model_rest.joblib")
model_young=load("artifacts/model_young.joblib")

scaler_rest=load("artifacts/scaler_rest.joblib")
scaler_young=load("artifacts/scaler_young.joblib")

def scale_dataframe_based_on_age(df):
    # Apply scaling based on the age condition
    if df['age'].iloc[0] <= 25:
        scaler_object=scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale=scaler_object['cols_to_scale']
    scaler=scaler_object['scaler']

    df[cols_to_scale]=scaler.transform(df[cols_to_scale])

    return df


def calculate_risk_scores(df):
    risk_scores_from_client = {
        'no disease': 0,
        'diabetes': 6,
        'high blood pressure': 6,
        'thyroid': 5,
        'heart disease': 8,
        "none": 0
    }
    # Ensure 'disease1' and 'disease2' columns are present
    df['disease1'] = df['disease1'].fillna('none')
    df['disease2'] = df['disease2'].fillna('none')

    # Initialize risk score for each row
    df['total_risk_score'] = 0

    # Loop through disease columns and calculate the total risk score
    for disease in ['disease1', 'disease2']:

        df['total_risk_score'] += df[disease].map(risk_scores_from_client)
    # Calculate normalized risk score
    max_score = df['total_risk_score'].max()
    min_score = df['total_risk_score'].min()
    if max_score != min_score:
        df['normalized_risk_score'] = (df['total_risk_score'] - min_score) / (max_score - min_score)
    else:
        df['normalized_risk_score'] = 0  # All values are the same

    # Drop unnecessary columns: disease1, disease2, total_risk_score
    df = df.drop(columns=['disease1', 'disease2', 'total_risk_score'])

    return df


def preprocess_input_data(input_data):
    # Initialize a dictionary for the DataFrame with expected columns
    data_dict = {
        'age': input_data['age'],
        'number_of_dependants': input_data['number_of_dependants'],
        'income_lakhs': input_data['income_lakhs'],
        'income_level':0,
        'insurance_plan':0,
        'genetical_risk': input_data['genetical_risk'],
        'total_risk_score': 0,  # Placeholder, will be computed later if needed
        'normalized_risk_score': 0,  # Placeholder, will be computed later if needed
        # Gender
        'gender_Male': 1 if input_data['gender'] == 'Male' else 0,
        # Region
        'region_Northwest': 1 if input_data['region'] == 'Northwest' else 0,
        'region_Southeast': 1 if input_data['region'] == 'Southeast' else 0,
        'region_Southwest': 1 if input_data['region'] == 'Southwest' else 0,
        # Marital Status
        'marital_status_Unmarried': 1 if input_data['marital_status'] == 'Unmarried' else 0,
        # BMI Category
        'bmi_category_Obesity': 1 if input_data['bmi_category'] == 'Obesity' else 0,
        'bmi_category_Overweight': 1 if input_data['bmi_category'] == 'Overweight' else 0,
        'bmi_category_Underweight': 1 if input_data['bmi_category'] == 'Underweight' else 0,
        # Smoking Status
        'smoking_status_Occasional': 1 if input_data['smoking_status'] == 'Occasional' else 0,
        'smoking_status_Regular': 1 if input_data['smoking_status'] == 'Regular' else 0,
        # Employment Status
        'employment_status_Salaried': 1 if input_data['employment_status'] == 'Salaried' else 0,
        'employment_status_Self-Employed': 1 if input_data['employment_status'] == 'Self-Employed' else 0
    }

    # Process 'income_level' into categories
    if input_data['income_lakhs'] >= 40:
        data_dict['income_level'] = 4
    elif input_data['income_lakhs'] >= 25:
        data_dict['income_level'] = 3
    elif input_data['income_lakhs'] >= 10:
        data_dict['income_level'] = 2
    else:  # '<10L'
        data_dict['income_level'] = 1

        # Process 'insurance_plan' into numerical values
    if input_data['insurance_plan'] == 'Bronze':
        data_dict['insurance_plan'] = 1
    elif input_data['insurance_plan'] == 'Silver':
        data_dict['insurance_plan'] = 2
    elif input_data['insurance_plan'] == 'Gold':
        data_dict['insurance_plan'] = 3

    # Process 'medical_history' to extract diseases (simplifying assumption: 2 diseases max)
    diseases = input_data['medical_history'].split(' & ') if ' & ' in input_data['medical_history'] else [
        input_data['medical_history']]
    data_dict['disease1'] = diseases[0].lower() if len(diseases) > 0 else 'none'
    data_dict['disease2'] = diseases[1].lower() if len(diseases) > 1 else 'none'

    # Convert the data_dict to a DataFrame
    df = pd.DataFrame([data_dict])

    #caliculating normalized risk score
    df=calculate_risk_scores(df)

    #scaling the numwrical values according to age , because we are using two different models
    df=scale_dataframe_based_on_age(df)

    return df



def predict(input_dict):
    input_df=preprocess_input_data(input_dict)
    input_df.drop("income_level", axis=1,inplace=True) #because of higher VIF score
    if input_dict['age']<= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction)
