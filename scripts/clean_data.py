import pandas as pd

def clean_data(input_file: str, output_file: str) -> None:
    """
    Cleans the data by removing rows with missing values and duplicates.
    
    Parameters:
    input_file (str): Path to the input CSV file.
    output_file (str): Path to save the cleaned CSV file.
    """
    # Load the data
    df = pd.read_csv(input_file)
    
    print(f"Initial data shape: {df.shape}")
    
    # Remove rows with missing values
    df_cleaned = df.drop(columns=['overview'])
    df_cleaned = df_cleaned.dropna()
    
    print(df_cleaned.shape)
    
    # Fix title formatting
    df_cleaned['title'].str.strip()
    
    print(df_cleaned.head())
    
    # Save the cleaned data
    df_cleaned.to_csv(output_file, index=False)
    
clean_data('data/raw/raw_movies.csv', 'data/cleaned/cleaned_movies.csv')
