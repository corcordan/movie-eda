# Exploratory Data Analysis of 10,000 Movies

## Project Overview
This project explores trends and patterns in a dataset of 10,000 movies using
release dates, original language, popularity, and voting metrics. The analysis
includes releases over decades, monthly and daily distributions, vote statistics,
and the relationship between vote average and popularity.

## Data Source
Kaggle – [10000 latest movies datasets 2025](https://www.kaggle.com/datasets/praveensoni06/1500-latest-movies-datasets-2025)
- Note: Despite the title, the dataset contains historical movies (as far back as 1897) 
  and upcoming releases through 2027.

## Key Insights
- Movie releases are heavily concentrated in recent decades, reflecting dataset bias.
- English dominates original language counts, with a long tail of other languages.
- Vote averages (after 1930) remain relatively stable over time despite changes in release volume.
- Popularity and vote average show only a weak relationship, suggesting popularity is not solely driven by user ratings.

## Live Dashboard
Explore the interactive version of this analysis:

[🎬 Movie EDA Dashboard](https://movie-eda.streamlit.app/)

## Notebook
View the full exploratory analysis:

[📓 EDA Notebook](https://github.com/corcordan/movie-eda/blob/main/notebooks/eda.ipynb)

## Installation

If you would like to run this locally:

1. Clone the repository
```bash
    git clone https://github.com/corcordan/movie-eda.git
    cd movie-eda
```

2. Create a virtual environment:
```bash
    python -m venv .venv
```

3. Activate the virtual environment:
macOS/Linux:
```bash
    source .venv/bin/activate
```

Windows (PowerShell):
```powershell
    .venv\Scripts\Activate.ps1
```

Windows (Command Prompt):
```cmd
    .venv\Scripts\activate.bat
```

4. Install dependencies
```bash
    pip install -r requirements.txt
```

5. Run the Streamlit dashboard:
```bash
    streamlit run dashboard.py
```
The application will open in your browser at http://localhost:8501.