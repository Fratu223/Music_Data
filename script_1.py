import streamlit as st
import pandas as pd

# Title of the app
st.title('CSV File Uploader')

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Here's the data from the uploaded CSV file:")
    st.write(df)