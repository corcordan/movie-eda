import sys
sys.path.append('../scripts/')

import streamlit as st
import pandas as pd
from scripts import data
from scripts import plots

st.set_page_config(
    page_title="Movie EDA Dashboard",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie EDA Dashboard")
st.markdown("""
Welcome to the Movie EDA Dashboard! This dashboard provides an exploratory data analysis of a movie dataset.
You can explore various aspects of the dataset including ratings, release years, languages, and more.

*Note: This*
""")

df = data.load_data('./data/cleaned/cleaned_movies.csv')
print(df.head())

st.write("The figure below represents the number of movies in the dataset that were released each decade")

fig = plots.plot_decades(df)
st.pyplot(fig, width=1000)

st.write("The figure below shows the number of movies released each year. While there may be ")

fig = plots.plot_years(df)
st.pyplot(fig, width=1000)

fig = plots.plot_months(df)
st.pyplot(fig, width=1000)

fig = plots.plot_days(df)
st.pyplot(fig, width=1000)

fig = plots.plot_langs(df)
st.pyplot(fig, width=1000)

fig = plots.plot_votes(df)
st.pyplot(fig, width=1000)

fig = plots.plot_votes_popularity(df)
st.pyplot(fig, width=1000)