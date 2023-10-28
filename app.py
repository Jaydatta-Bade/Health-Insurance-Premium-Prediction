import streamlit as st
import joblib

# Load the saved model
model_filename = 'regression_model.joblib'
loaded_model = joblib.load(model_filename)

st.title('Health Insurance Premium Prediction')

# Define input fields
age = st.number_input('Age', min_value=0, max_value=100)
sex = st.selectbox('Sex', ['Male', 'Female'])
bmi = st.number_input('BMI', min_value=0.0, max_value=100.0)
children = st.number_input('Number of Children', min_value=0, max_value=10)
smoker = st.selectbox('Smoker', ['No', 'Yes'])
region = st.selectbox('Region', ['Northeast', 'Northwest', 'Southeast', 'Southwest'])

# Convert user input to appropriate format
sex = 0 if sex == 'Male' else 1
smoker = 0 if smoker == 'No' else 1
region = ['Northeast', 'Northwest', 'Southeast', 'Southwest'].index(region)

# Make predictions
if st.button('Predict'):
    input_data = [[age, sex, bmi, children, smoker, region]]
    prediction = loaded_model.predict(input_data)
    st.write(f'Predicted Insurance Charges: ₹{prediction[0]:.2f}')
