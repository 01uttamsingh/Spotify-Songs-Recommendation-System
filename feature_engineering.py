import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the cleaned dataset
spotify_df = pd.read_csv("spotify.csv")

# Step 1: Feature Engineering
# Aggregate total listening time per song
song_playtime = spotify_df.groupby(['track_name', 'artist_name']).agg({'minutes_played': 'sum'}).reset_index()

# Step 2: Text-Based Similarity Using TF-IDF (for song & artist matching)
# Combine 'track_name' and 'artist_name' for a more comprehensive feature
song_playtime['track_artist'] = song_playtime['track_name'] + " " + song_playtime['artist_name']

# Apply TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(song_playtime['track_artist'])

# Step 3: Cosine Similarity Calculation
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend similar songs
def get_recommendations(track_name, cosine_sim=cosine_sim):
    # Get index of the song that matches the title
    idx = song_playtime[song_playtime['track_name'] == track_name].index[0]
    
    # Get pairwise similarity scores of all songs with that song
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the songs based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 10 most similar songs
    sim_scores = sim_scores[1:11]
    song_indices = [i[0] for i in sim_scores]
    
    # Return the top 10 most similar songs
    return song_playtime.iloc[song_indices][['track_name', 'artist_name', 'minutes_played']]

# Example: Get recommendations for a song
recommended_songs = get_recommendations("Shape of You")
print(recommended_songs)
