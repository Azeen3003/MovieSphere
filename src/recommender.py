import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load processed data
data_path = "notebooks/processed_movies.csv"
similarity_path = "notebooks/cosine_similarity.npy"

df = pd.read_csv(data_path)

# Ensure cosine similarity matrix exists or recompute if necessary
if os.path.exists(similarity_path):
    cosine_sim = np.load(similarity_path)
else:
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Overview'].fillna(""))
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    np.save(similarity_path, cosine_sim)

def get_recommendations(title, num_recommendations=5):
    if title not in df['Title'].values:
        return []
    
    idx = df[df['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]  # Exclude itself
    
    movie_indices = [i[0] for i in sim_scores]
    recommendations = df.iloc[movie_indices][['Title', 'Poster_Url', 'Release_Date']]
    recommendations['Release_Year'] = pd.to_datetime(recommendations['Release_Date'], errors='coerce').dt.year.fillna('Unknown').astype(str)
    
    return list(zip(recommendations['Title'], recommendations['Poster_Url'], recommendations['Release_Year']))
