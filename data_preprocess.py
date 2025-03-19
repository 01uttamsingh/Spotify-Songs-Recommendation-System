import pandas as pd

# Load dataset
file_path = "spotify_history.csv"  # Update the path if needed
spotify_df = pd.read_csv(file_path)

# Convert 'ts' column to datetime format
spotify_df['ts'] = pd.to_datetime(spotify_df['ts'])

# Fill missing values in 'reason_start' and 'reason_end' with 'unknown'
spotify_df['reason_start'].fillna('unknown', inplace=True)
spotify_df['reason_end'].fillna('unknown', inplace=True)

# Convert 'ms_played' from milliseconds to minutes (rounded to 2 decimal places)
spotify_df['minutes_played'] = (spotify_df['ms_played'] / 60000).round(2)

# Drop duplicates
spotify_df.drop_duplicates(inplace=True)

# Save cleaned dataset
spotify_df.to_csv("spotify.csv", index=False)

# Display basic info
print(spotify_df.info())
print(spotify_df.head())
