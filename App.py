import numpy as np 
import pandas as pd 
import pickle as pkl 
import streamlit as st 

model = pkl.load(open('MIPML.pkl', 'rb'))

st.header('Medical Insurance Price Predictor') 
#streamlit run App.py

gender = st.selectbox('Choose Gender', ['Female', 'Male'])
smoker = st.selectbox('Are you a smoker?', ['Yes', 'No'])
region = st.selectbox("Choose Region", ['Southeast', 'Southwest', 'Northeast', 'Northwest'])
age = st.slider('Enter Age', 5, 80)
bmi = st.slider('Enter BMI', 5, 100)
children = st.slider('Choose No. of Children', 0, 5)

if gender == 'Female':
    gender = 0
else:
    gender = 1
    
if smoker == 'No':
    smoker = 0
else:
    smoker = 1

if region =='Southeast':
    region = 0
if region =='Southwest':
    region = 1
if region =='Northeast':
    region = 2
else:
    region = 3
    
input_data = (age, gender, bmi, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)

predicted_price = model.predict(input_data)
display_string = 'Insurance Price will be' + str(predicted_price)+'USD Dollars'

st.markdown(display_string)