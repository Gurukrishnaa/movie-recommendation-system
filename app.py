from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse.linalg import svds
import numpy as np
import os

app = Flask(__name__)

# Load the dataset
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# Create user-item matrix
user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Compute user-user similarity matrix
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Compute item-item similarity matrix
item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Function for user-based collaborative filtering
def recommend_movies_user_based(user_id, n_recommendations=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]
    similar_users_ratings = user_item_matrix.loc[similar_users.index]
    weighted_ratings = similar_users_ratings.mul(similar_users, axis=0)
    recommended_movies = weighted_ratings.sum().sort_values(ascending=False)
    recommended_movies = recommended_movies[user_item_matrix.loc[user_id] == 0]
    return recommended_movies.head(n_recommendations)

# Function for item-based collaborative filtering
def recommend_movies_item_based(user_id, n_recommendations=5):
    user_ratings = user_item_matrix.loc[user_id]
    rated_movies = user_ratings[user_ratings > 0].index
    similar_movies = item_similarity_df[rated_movies].sum(axis=1).sort_values(ascending=False)
    similar_movies = similar_movies[user_ratings == 0]
    return similar_movies.head(n_recommendations)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation page
@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    algorithm = request.form['algorithm']
    
    if algorithm == 'user_based':
        recommendations = recommend_movies_user_based(user_id)
    else:
        recommendations = recommend_movies_item_based(user_id)
    
    # Get movie titles for recommendations
    recommended_movies = movies[movies['movieId'].isin(recommendations.index)]
    recommended_movies = recommended_movies.set_index('movieId').loc[recommendations.index]
    
    return render_template('recommendations.html', user_id=user_id, recommendations=recommended_movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))