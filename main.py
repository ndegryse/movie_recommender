import pandas as pd

#rating wa ssaved in a tab seperated file, movie was saved in a pipe seperated file
#merged ratings and movie_titles dataframe on movie_id to create total_data dataframe
ratings = pd.read_csv("ml-100k/u.data", delimiter="\t", names=["user_id", "movie_id", "rating", "timestamp"])
movie_titles = pd.read_csv("ml-100k/u.item", delimiter="|", names=["movie_id", "title"], usecols=[0,1], encoding='latin-1')
total_data = ratings.merge(movie_titles, on ="movie_id")

#created a matrix with user_id as index, title as columns and rating as values
user_movie_matrix = total_data.pivot_table(index="user_id", columns="title", values="rating")

#converted matrix to csv file
user_movie_matrix.to_csv("user_movie_matrix.csv")

#cleaned the matrix by filling NaN values with 0 and saved to another csv file for clarity
user_movie_matrix_filled = user_movie_matrix.fillna(0)
user_movie_matrix_filled.to_csv("user_movie_matrix_filled.csv")
