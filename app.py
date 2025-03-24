import streamlit as st
import pandas as pd
import numpy as np
import time
from src.recommender import get_recommendations  # Import function from utils.py

# Load processed data
df = pd.read_csv("notebooks/processed_movies.csv")

# Streamlit UI
st.set_page_config(page_title="MovieSphere - Movie Recommender", layout="wide")

# Header Banner
left, centre, right = st.columns(3)
with centre:
    st.image("src/logo.png")

st.markdown("""
    <h1 style='text-align: center; font-size: 50px; font-weight: bold;'>🎬 MovieSphere</h1>
    <h3 style='text-align: center;'>Find Your Next Favorite Movie!</h3>
    """, unsafe_allow_html=True)

# Auto-suggest movie title
def movie_search():
    movie_list = df['Title'].tolist()
    return movie_list

st.markdown("""
    <style>
    .stSelectbox > div[data-baseweb="select"] {
        font-size: 18px !important;
        padding: 10px !important;
    }
     .stButton > button {
        display: block;
        margin: 20px auto;
        font-size: 20px;
        padding: 12px 25px;
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #d43f3f;
        color: white !important;
    }
    .movie-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

selected_movie = st.selectbox("🔍 Search for a movie:", movie_search(), placeholder="Type a movie name...")

st.divider()
if st.button("🎥 Recommend Movies"):  # When user clicks the button
    with st.spinner("Finding your next favorite movies..."):
        time.sleep(1.5)  # Simulate processing delay
        recommendations = get_recommendations(selected_movie)
    
    if recommendations:
        st.subheader("✨ Recommended Movies for You:")
        st.divider()
        cols = st.columns(5)  # Create 5 columns for posters
        
        for i, (movie, poster_url, release_year) in enumerate(recommendations):
            with cols[i]:
                st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                st.image(poster_url, use_container_width=True)
                st.markdown(f"**🎬 {movie} ({release_year})**", unsafe_allow_html=True)
                st.markdown(f"[🔗 More Info on IMDb](https://www.imdb.com/find?q={movie.replace(' ', '+')})", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("❌ No recommendations found. Try another movie!")
