# This code lists movies from a library on Plex

import pandas as pd
from plexapi.server import PlexServer

baseurl = 'http://<your-url>'
token = '<your-token>'
plex = PlexServer(baseurl, token)

movies = plex.library.section('your-section')

# Get all movies from the library
movies = filmes.all()

# Creating a list of dictionaries containing data from each movie
movie_list = []
for movie in movies:
    movie_dict = {
        'title': movie.title,
        'original title': movie.originalTitle,
        'year': movie.year,
        'rating': movie.rating,
        'added at': movie.addedAt
    }
    movie_list.append(movie_dict)
    

# Converting list of dictionaries to Pandas dataframe
df = pd.DataFrame(movie_list)

# Saving dataframe as CSV
df.to_csv('movies.csv', index=False)
