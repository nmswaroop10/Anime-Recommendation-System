import streamlit as st
import pickle

animes = pickle.load(open("animes_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
animes_list = animes['title'].values

st.header("Anime Recommendation System")
selectvalue = st.selectbox("Select Animes From Drop Down", animes_list)


def recommend(anime):
    index = animes[animes['title'] == anime].index[0]
    distance = sorted(
        list(
            enumerate(
                similarity[index])),
        reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        recommend_movie.append(animes.iloc[i[0]].title)
        recommend_poster.append(animes.iloc[i[0]].image)
    return recommend_movie, recommend_poster


if st.button("Show Recommendations"):
    anime_name, anime_poster = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(anime_name[0])
        st.image(anime_poster[0])
    with col2:
        st.text(anime_name[1])
        st.image(anime_poster[1])
    with col3:
        st.text(anime_name[2])
        st.image(anime_poster[2])
    with col4:
        st.text(anime_name[3])
        st.image(anime_poster[3])
    with col5:
        st.text(anime_name[4])
        st.image(anime_poster[4])
