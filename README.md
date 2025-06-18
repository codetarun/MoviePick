# 🎬 MoviePick - A Movie Recommendation System

This is a content-based movie recommendation system built using Python. It recommends movies similar to your favorite ones using cosine similarity on movie data.


## 🚀 Features

- Recommend movies similar to a selected title
- Uses `pandas`, `scikit-learn`, and `gdown`
- Lightweight and easy to deploy


### 📂 Project Structure

├── app.py # Main application file
├── movie_dict.pkl # Contains movie metadata (not tracked in GitHub)
├── similarity.pkl # Similarity matrix (downloaded via gdown)
├── .gitignore
└── README.md


#### 🔧 Setup Instructions

1. **Clone the Repository** :
```bash
git clone https://github.com/codetarun/MoviePick.git
cd MoviePick

2. Create Virtual Environment & Install Dependencies :
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

3. Run the App :
python app.py


📥 Download similarity.pkl :

This file is large, so it's not included in the repo. It will automatically be downloaded from Google Drive using gdown when the app runs.


🧠 Technologies Used :

Python
Pandas
NumPy
NLP(Natural Language Processing)
Machine Learning (Scikit-learn)
Cosine Similarity
Pickle
gdown
Jupiter Notebook
VS Code
GitHub

🙏 Acknowledgements :

Thanks to TMDB for the movie data.


📬 Contact :

Email: tarunn2501@gmail.com