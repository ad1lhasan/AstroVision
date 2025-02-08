import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.title('Planet Prediction')
st.subheader('Upload a CSV file to predict')

uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
  
    st.write(df)

    predictions = loaded_model.predict(df)
  
    st.write('Predictions:')
    st.write(predictions)
else:
    st.write('Please upload a CSV file to proceed.')