import pandas as pd

#rating was saved in a tab separated file, movie was saved in a pipe separated file
#merged ratings and movie_titles dataframes on movie_id to create total_data dataframe
ratings = pd.read_csv("ml-100k/u.data", delimiter="\t", names=["user_id", "movie_id", "rating", "timestamp"])
movie_titles = pd.read_csv("ml-100k/u.item", delimiter="|", names=["movie_id", "title"], usecols=[0,1], encoding='latin-1')
total_data = ratings.merge(movie_titles, on="movie_id")

#created a matrix with user_id as index, title as columns and rating as values
user_movie_matrix = total_data.pivot_table(index="user_id", columns="title", values="rating")

#converted matrix to csv file
user_movie_matrix.to_csv("user_movie_matrix.csv")

#cleaned the matrix by filling NaN values with 0 and saved to another csv file for visual clarity 
user_movie_matrix_filled = user_movie_matrix.fillna(0)
user_movie_matrix_filled.to_csv("user_movie_matrix_filled.csv") 

#raw data layout analysis
n_users = len(ratings.user_id.unique())
print(f"Number of unique users in the dataset: {n_users}")
n_items = len(ratings.movie_id.unique())
print(f"Number of unique movies in the dataset: {n_items}")
print("-------" * 5)
print(f"The full rating matrix will have: {n_users * n_items} elements")
print(f"The number of ratings in the dataset is: {len(ratings)}")
print(f"The sparsity of the user-movie matrrix is: {len(ratings) / (n_users * n_items) * 100:.2f}%")
print("-------" * 5)