import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Spotify Playlist Data Analysis')

# CSV file info
st.write("For requiring the CSV file of the playlist, please visit this site https://exportify.net/")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV playlist file", type="csv")

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Here's the tracks from the playlist:")
    st.write(df[['Track Name', 'Album Name', 'Artist Name(s)']])

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

    # Calculate the average duration in ms of songs in the playlist
    average_duration = df.loc[:,'Duration (ms)'].mean()

    # Display the average duration in ms of songs the playlist
    st.write("Average duration (ms) of songs in the playlist")
    st.write(average_duration)

    # Calculate the average danceability of the playlist
    average_danceability = df.loc[:,'Danceability'].mean()

    # Display the average danceability of the playlist
    st.write("Average danceability of the playlist")
    st.write(average_danceability)

    # Calculate the average energy of the playlist
    average_energy = df.loc[:,'Energy'].mean()

    # Display the average energy of the playlist
    st.write("Average energy of the playlist")
    st.write(average_energy)

    # Retrive list of artist names
    artist_names = list(df['Artist Name(s)'])

    # Empty list for main and featuring artists
    new_artist_names = []

    # Separate main and featuring artists
    for artist in artist_names:
        new_artist_list = artist.split(',')
        for i in range(0, len(new_artist_list)):
            new_artist_names.append(new_artist_list[i])

    # New DataFrame with main and featuring artists separated
    new_df = pd.DataFrame({'Names':new_artist_names})

    # Calculate the value couts for the artist name
    artist_value_counts = new_df['Names'].value_counts()

    # Plot the artist name by value counts
    st.write('Value counts for artist name:')
    st.bar_chart(artist_value_counts)

    # Retrive list of genres
    genres = list(df['Genres'].dropna())

    # Empty list for splitting multiple genres 
    new_genres = []

    # Separate multiple genres
    for genre in genres:
        genres_list = genre.split(',')
        for i in range(0, len(genres_list)):
            new_genres.append(genres_list[i])

    # New DataFrame with multiple genres separated
    new_df_2 = pd.DataFrame({'Genres':new_genres})

    # Calculate the value couts for the genres
    genres_value_counts = new_df_2['Genres'].value_counts()

    # Plot the genres by value counts
    st.write('Value counts for genres:')
    st.bar_chart(genres_value_counts)