import pandas as pd
import matplotlib.pyplot as plt


def plot_decades(df: pd.DataFrame):
    years = df.groupby('release_year').size()
    decades = years.groupby((years.index // 10) * 10).sum()

    fig, ax = plt.subplots(figsize=(10, 6))

    decades.plot(kind='bar', ax=ax, color='skyblue')

    ax.set_title('Number of Releases per Decade')
    ax.set_xlabel('Decade')
    ax.set_ylabel('Number of Releases')
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()

    return fig


def plot_years(df: pd.DataFrame):
    years = df.groupby('release_year').size()

    fig, ax = plt.subplots(figsize=(12, 6))

    years.plot(kind='line', ax=ax, color='lightgreen')

    ax.set_title('Number of Releases per Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Releases')
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()

    return fig


def plot_months(df: pd.DataFrame):
    months = df.groupby('release_month').size().reindex(range(1, 13), fill_value=0)
    months.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, ax = plt.subplots(figsize=(10, 6))

    months.plot(kind='bar', ax=ax, color='salmon')

    ax.set_title('Number of Releases per Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Releases')
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()

    return fig


def plot_days(df: pd.DataFrame):
    days = df.groupby('release_day').size()

    fig, ax = plt.subplots(figsize=(10, 6))

    days.plot(kind='bar', ax=ax, color='orchid')

    ax.set_title('Number of Releases per Day of Month')
    ax.set_xlabel('Day of Month')
    ax.set_ylabel('Number of Releases')
    ax.tick_params(axis='x', rotation=0)

    fig.tight_layout()

    return fig


def plot_langs(df: pd.DataFrame):
    langs = (
        df.groupby('original_language')
          .size()
          .sort_values(ascending=False)
          .head(10)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    langs.plot(kind='bar', ax=ax, color='gold')

    ax.set_title('Top 10 Original Languages of Movies')
    ax.set_xlabel('Language')
    ax.set_ylabel('Number of Movies')
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()

    return fig


def plot_votes(df: pd.DataFrame, stats: list[str] = ["Max", "Mean", "Median", "Min"]):
    votes = df.groupby('release_year')['vote_average']

    fig, ax = plt.subplots(figsize=(12, 6))
    
    if "Max" in stats:
        ax.plot(votes.max().index, votes.max(), label='Max', color='red')
        
    if "Mean" in stats:
        ax.plot(votes.mean().index, votes.mean(), label='Mean', color='blue')
        
    if "Median" in stats:
        ax.plot(votes.median().index, votes.median(), label='Median', color='green')
    
    if "Min" in stats:
        ax.plot(votes.min().index, votes.min(), label='Min', color='orange')

    ax.set_title('Vote Averages by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Vote Average')
    ax.legend()
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()

    return fig


def plot_votes_popularity(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df['vote_average'],
        df['popularity'],
        alpha=0.5,
        color='teal'
    )

    ax.set_title('Vote Average vs Popularity')
    ax.set_xlabel('Vote Average')
    ax.set_ylabel('Popularity')

    fig.tight_layout()

    return fig