# Importing Major Modules

import pickle
import pandas as pd
import streamlit as st

#Load the Data

data = pickle.load(open('movie_dict.pkl', mode = 'rb'))
data = pd.DataFrame(data)

similarity = pickle.load(open('similarity.pkl', mode = 'rb'))
print(similarity)

# Recommendation Function

def recommend(movie):
    
    recommended_movies = []
    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x: x[1])[1:6]
    
    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)
    return recommended_movies

# Streamlit based Web-App

st.title('MOVIEPICK:clapper:')
st.write('This is a simple movie recommendation system based on the similarity between movies.')

selected_movie = st.selectbox("Select a movie to get recommendations",(data['title'].values))
btn = st.button('Recommend')

# Button

if btn:
    top_five_movies = recommend(selected_movie)
    
    for i in top_five_movies:
        st.write(i)
