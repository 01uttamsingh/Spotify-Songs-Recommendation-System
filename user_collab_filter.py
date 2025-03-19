import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load cleaned dataset
spotify_df = pd.read_csv("main_spotify.csv")

# Convert usernames to lowercase for case-insensitive matching
spotify_df['username'] = spotify_df['username'].str.lower()

# Step 1: Create a user-song interaction matrix
user_song_matrix = spotify_df.pivot_table(index='username', columns='track_name', values='minutes_played', aggfunc='sum', fill_value=0)

# Step 2: Standardize the data (important for similarity)
scaler = StandardScaler()
user_song_matrix_scaled = scaler.fit_transform(user_song_matrix)

# Step 3: Calculate cosine similarity between users
user_similarity = cosine_similarity(user_song_matrix_scaled)

# Step 4: Recommend songs based on similar users
def recommend_songs_user_based(username, user_similarity, user_song_matrix, top_n=10):
    # Convert username to lowercase for case-insensitive matching
    username = username.strip().lower()
    
    # Get index of the user
    try:
        user_idx = user_song_matrix.index.get_loc(username)
    except KeyError:
        print(f"Username '{username}' not found in the matrix.")
        return None
    
    # Get similarity scores of this user with all other users
    sim_scores = list(enumerate(user_similarity[user_idx]))
    
    # Sort users based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top similar users (excluding the user themselves)
    similar_users = [i[0] for i in sim_scores[1:top_n+1]]
    
    # If no similar users found, recommend popular songs instead
    if not similar_users:
        print("No similar users found. Recommending popular songs instead.")
        return user_song_matrix.sum(axis=0).sort_values(ascending=False).head(top_n)
    
    # Aggregate songs that are liked by similar users
    similar_user_ratings = user_song_matrix.iloc[similar_users]
    
    # Aggregate scores and recommend the top songs
    recommended_songs = similar_user_ratings.sum(axis=0).sort_values(ascending=False).head(top_n)
    
    # If no songs were recommended, recommend the user’s most played tracks
    if recommended_songs.empty:
        print("No songs recommended. Returning user's most played songs instead.")
        return user_song_matrix.loc[username].sort_values(ascending=False).head(top_n)
    
    return recommended_songs

# Example: Get song recommendations for a specific user
username = input("Enter Username for recommendations: ").strip().lower()
recommended_songs_user = recommend_songs_user_based(username, user_similarity, user_song_matrix)

if recommended_songs_user is not None:
    print(f"Recommended songs for {username}:")
    print(recommended_songs_user)
