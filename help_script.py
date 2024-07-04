import pandas as pd

df = pd.read_csv('test_table_2.csv')

artist_names = list(df['Artist Name(s)'])

new_artist_names = []

for artist in artist_names:
    new_artist_list = artist.split(',')
    for i in range(0, len(new_artist_list)):
        new_artist_names.append(new_artist_list[i])

new_df = pd.DataFrame({'Names':new_artist_names})

print(new_df['Names'].value_counts())

genres = list(df['Genres'])

print(genres)