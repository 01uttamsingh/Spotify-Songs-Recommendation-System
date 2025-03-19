from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load cleaned dataset
spotify_df = pd.read_csv("main_spotify.csv")

# Convert usernames to lowercase for case-insensitive matching
spotify_df['username'] = spotify_df['username'].str.lower()

# Create a user-song interaction matrix
user_song_matrix = spotify_df.pivot_table(index='username', columns='track_name', values='minutes_played', aggfunc='sum', fill_value=0)

# Standardize the data
scaler = StandardScaler()
user_song_matrix_scaled = scaler.fit_transform(user_song_matrix)

# Compute similarity
user_similarity = cosine_similarity(user_song_matrix_scaled)

def recommend_songs(username, top_n=10):
    username = username.strip().lower()  # Make input case-insensitive
    
    if username not in user_song_matrix.index:
        return []  # Return empty list if username not found
    
    user_idx = user_song_matrix.index.get_loc(username)
    sim_scores = list(enumerate(user_similarity[user_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    similar_users = [i[0] for i in sim_scores[1:top_n+1]]
    similar_user_ratings = user_song_matrix.iloc[similar_users]
    recommended_songs = similar_user_ratings.sum(axis=0).sort_values(ascending=False).head(top_n)
    return recommended_songs.index.tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    username = request.form['username']
    recommendations = recommend_songs(username)
    
    # Pass 'songs' to match 'result.html'
    return render_template('result.html', songs=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
