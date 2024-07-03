import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Spotify Playlist Data Analysis')

# File uploader
uploaded_file = st.file_uploader("Choose a CSV playlist file", type="csv")

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Here's the data from the uploaded CSV playlist file:")
    st.write(df)

    # Calculate the average tempo of the playlist
    average_tempo = df.loc[:,'Tempo'].mean()

    # Display the average tempo of the playlist
    st.write("Average tempo of the playlist")
    st.write(average_tempo)

    # Calculate the average popularity of the playlist
    average_popularity = df.loc[:,'Popularity'].mean()

    # Display the average popularity of the playlist
    st.write("Average popularity of the playlist")
    st.write(average_popularity)

    # Calculate the value couts for the artist name
    artist_value_counts = df['Artist Name(s)'].value_counts()

    # Plot the artist name by value counts
    st.write('Value counts for artist name:')
    st.bar_chart(artist_value_counts)