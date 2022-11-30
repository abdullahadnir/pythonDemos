import pandas as pd

df = pd.read_csv('imdb.csv')
result = df

result= df.head()
result= df.head(10)
result = df.tail()
result = df.tail(10)
result = df['Title']
result = df['Title'].head()
result = df[['Title','Ratings.Value']].head()
result = df[['Title','Ratings.Value']].tail(7)
result = df[5:10][['Title','Ratings.Value']]

result = df[df["imdbRating"] >= 8.0][['Title','Ratings.Value']].head(50)

result = df[(df["Year"] >= 2014) & (df["Year"] <= 2015)][['Title','Year']]

result = df[(df['Metascore'] >= 100) | ((df["imdbRating"] >= 8.5) & (df["imdbRating"] <= 9.0))][['Title','imdbRating','Metascore']]










print(result)
