import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("notebooks/processed_movies.csv")
cosine_sim = np.load("notebooks/cosine_similarity.npy")

# Function to get recommendations
def get_recommendations(title, num_recommendations=5):
    if title not in df['Title'].values:
        return []

    # Get index of the movie
    idx = df[df['Title'] == title].index[0]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]  # Exclude itself

    # Get movie titles & poster URLs
    movie_indices = [i[0] for i in sim_scores]
    
    recommendations = []
    for i in movie_indices:
        movie_name = df.iloc[i]['Title']
        poster_url = df.iloc[i]['Poster_Url']  # Assuming column name is Poster_Url
        
        # Extract the year from Release_Date column
        release_date = df.iloc[i]['Release_Date']
        release_year = pd.to_datetime(release_date, errors='coerce').year if pd.notna(release_date) else "N/A"
        
        recommendations.append((movie_name, poster_url, release_year))
    
    return recommendations
