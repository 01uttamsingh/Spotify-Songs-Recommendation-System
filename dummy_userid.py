import pandas as pd
import numpy as np

# Load your dataset
spotify_df = pd.read_csv("spotify.csv")

# Step 1: Add a dummy 'user_id' column (randomly assigning user IDs to each row)
# For example, randomly assign user IDs from 1 to 1000 (adjust as needed)
spotify_df['user_id'] = np.random.randint(1, 1001, size=len(spotify_df))

# Step 2: Save the updated dataset with dummy 'user_id' to a new CSV file
spotify_df.to_csv("main_spotify.csv", index=False)

# Print the first few rows to check the added 'user_id' column
print(spotify_df.head())
