import pandas as pd

df = pd.read_csv('IMDB Top 250 Movies.csv')

df = df.drop(['rank','tagline','budget','box_office','casts','directors','writers'], axis=1)

df[['gen1','gen2','gen3']] = df['genre'].str.split(',',expand=True)

df.fillna(value = 0,inplace = True)

def get_movie_recommendations(genre_list,df):

  if len(genre_list) > 3:
    raise ValueError('You can only choose up to 3 Genres')

  elif len(genre_list) == 1:

    single_genre = df[
        ((df['gen1'] == genre_list[0]) & (df['gen2'] == 0) & (df['gen3'] == 0))
    ]

    single_genre = single_genre.drop_duplicates(subset=['name']).sample(frac=1)

    recommendations = single_genre.head(3)['name'].tolist()

  elif len(genre_list) == 2:

    two_genres = df[
        ((df['gen1'] == genre_list[0]) | (df['gen2'] == genre_list[0]) & (df['gen3'] == 0)) &
        ((df['gen1'] == genre_list[1]) | (df['gen2'] == genre_list[1]) & (df['gen3'] == 0))
    ]

    two_genres = two_genres.drop_duplicates(subset=['name']).sample(frac=1)

    recommendations = two_genres.head(3)['name'].tolist()

  else:

    three_genres = df[
        (df['gen1'].isin(genre_list) & df['gen2'].isin(genre_list) & df['gen3'].isin(genre_list))
    ]

    three_genres = three_genres.drop_duplicates(subset=['name']).sample(frac=1)

    recommendations = three_genres.head(3)['name'].tolist()

  if not recommendations:

    print("Sorry, there are no recommendations for the provided Genres. If you have only provided one Genre, there might not be a movie of that specific Genre in IMDB's Top 250 List. If you have provided more than one Genre, there might not be any movies that match that combination of Genres in IMDB's Top 250 List")

  return recommendations

# Do not amend any of the above code

Your_provided_Genres = ['Enter your first Genre','Enter your second Genre', 'Enter your third Genre']

# Do not amend any of the below code

Your_Movie_Recommendations = get_movie_recommendations(Your_provided_Genres, df)

print(f"\nMovie Recommendations based on your provided Genres {Your_provided_Genres}:")
for i, name in enumerate(Your_Movie_Recommendations, 1):
    print(f"{i}. {name}")

