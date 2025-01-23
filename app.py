import requests
import streamlit as st
import pickle
import pandas as pd


# Poster fetch function
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b7e0da4255863382860eb7727db6fa4f&language=en-US")
    data = response.json()
    if 'poster_path' in data:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return None


# Recommendation function
def recommand(movie):
    if movie not in movies['title'].values:
        return ["Movie not found."]

    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommanded_movies = []
    recommanded_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommanded_movies.append(movies.iloc[i[0]].title)
        recommanded_movies_poster.append(fetch_poster(movie_id))

    return recommanded_movies, recommanded_movies_poster


# Load the movie dictionary and similarity matrix
movie_dict = pickle.load(open("movie_dict.pkl", 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# Streamlit UI
st.title("Movie Recommendation System")

# Movie selection dropdown
selected_movie_name = st.selectbox("Enter The Name of Movie", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommand(selected_movie_name)

    # Display movie names and posters in columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0], use_container_width=True)
        st.text(names[0])
    with col2:
        st.image(posters[1], use_container_width=True)
        st.text(names[1])
    with col3:
        st.image(posters[2], use_container_width=True)
        st.text(names[2])
    with col4:
        st.image(posters[3], use_container_width=True)
        st.text(names[3])
    with col5:
        st.image(posters[4], use_container_width=True)
        st.text(names[4])
