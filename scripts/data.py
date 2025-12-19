import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['release_year'] = pd.to_datetime(df['release_date']).dt.year
    df['release_month'] = pd.to_datetime(df['release_date']).dt.month
    df['release_day'] = pd.to_datetime(df['release_date']).dt.day
    return df