import streamlit as st
import pandas as pd
import scripts.data as data
import scripts.plots as plots

# Load the data
df = data.load_data('./data/cleaned/cleaned_movies.csv')

# Set page info
st.set_page_config(
    page_title="Movie EDA Dashboard",
    page_icon="🎬",
    layout="wide"
)

# Intro
st.title("Exploratory Data Analysis of 10,000 Movies")
st.markdown("""
This dashboard explores trends and patterns in a dataset of 10,000 movies using
release dates, language, popularity, and voting metrics.
""")

# Expander with info
with st.expander("Dataset Information & Assumptions"):
    st.markdown("""
    - Source: Kaggle – *10000 latest movies datasets 2025*
    - Although labeled as "latest movies 2025", the dataset includes movies dating back to 1897
      and some upcoming releases through 2027.
    - Based on available fields, this appears to be a general movie metadata collection
      likely sourced from TMDB or IMDb.
    - This analysis reflects trends **within this dataset only**, not total historical releases.
    """)
    
# Sidebar
st.sidebar.header("Filters")

year_range = st.sidebar.slider(
    "Release Year Range",
    df["release_year"].min(),
    df["release_year"].max(),
    (2000, 2025)
)

# New df based on sidebar slider year range
filtered_df = df[
    (df["release_year"] >= year_range[0]) &
    (df["release_year"] <= year_range[1])
]

# Decade, year, month, and day plots
st.subheader("Release Trends Over Time")
st.markdown("Distribution of movie releases by decade, year, month, and day.")


fig = plots.plot_decades(filtered_df)
st.pyplot(fig)

fig = plots.plot_years(filtered_df)
st.pyplot(fig)

fig = plots.plot_months(filtered_df)
st.pyplot(fig)

fig = plots.plot_days(filtered_df)
st.pyplot(fig)

st.subheader("Original Language Distribution")
st.markdown("Top 10 original languages by number of movies.")

fig = plots.plot_langs(filtered_df)
st.pyplot(fig)

st.subheader("Vote Averages by Year")
st.markdown("""
Comparison of mean, median, minimum, and maximum vote averages by release year.
""")

stat_options = st.multiselect(
    "Vote Statistics",
    options=["Mean", "Median", "Max", "Min"],
    default=["Mean", "Median"]
)

fig = plots.plot_votes(filtered_df, stat_options)
st.pyplot(fig)

st.subheader("Popularity vs Vote Average")
st.markdown("""
Exploring the relationship between user ratings and movie popularity.
""")

fig = plots.plot_votes_popularity(filtered_df)
st.pyplot(fig)

# Insights
st.subheader("Key Insights")

st.markdown("""
- Movie releases are heavily concentrated in recent decades, reflecting dataset bias.
- English dominates original language counts, with a long tail of other languages.
- Vote averages (after 1930) remain relatively stable over time despite large changes in release volume.
- Popularity and vote average show only a weak relationship, suggesting popularity is not
  solely driven by user ratings.
""")

# Footer
st.markdown("---")
st.markdown("""
**Built by Daniel Corcoran**  
- [GitHub](https://github.com/corcordan) | [Portfolio](https://www.corcordan.com)
""")
