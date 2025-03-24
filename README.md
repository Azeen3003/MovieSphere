# 🎬 MovieSphere

## 📌 Overview
MovieSphere is a **content-based movie recommendation system** built using **Streamlit**. It helps users discover new movies based on plot similarities, displaying posters and release years for a better user experience.

## ✨ Features
- 🔍 **Movie Search with Auto-Suggestions**
- 🎥 **Personalized Movie Recommendations**
- 🖼️ **Movie Posters & Release Years**
- 🎭 **Hollywood & Bollywood Movie Support**
- 🌟 **IMDb Links for More Information**
- ⚡ **Fast & Interactive UI**

## 🚀 Installation
To run MovieSphere locally, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Azeen3003/MovieSphere.git
cd MovieSphere
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** 🌐 (for the web interface)
- **NumPy & Pandas** 📊 (for data processing)
- **TF-IDF & Cosine Similarity** 🧠 (for recommendations)

## 🔎 How It Works
1. **Preprocessing**: The dataset is cleaned, and TF-IDF vectorization is applied to movie plots.
2. **Similarity Calculation**: Cosine similarity is used to find movies with similar plot summaries.
3. **User Input**: The user searches for a movie title.
4. **Recommendation**: The app finds and displays 5 similar movies along with posters and release years.

## 🌐 Demo
🚀 **Live Deployment**: *(Coming Soon!)*

## 📸 Screenshots
tba

## 🤝 Contributing
Want to improve MovieSphere? Feel free to fork the repo and submit pull requests! 🎉

## 📜 License
This project is licensed under the MIT License.

---
🎬 **MovieSphere** | Built with ❤️ using Streamlit