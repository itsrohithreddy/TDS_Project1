import pandas as pd

def analyze_repo_features(csv_file):
    df = pd.read_csv(csv_file)
    if df['has_projects'].dtype == 'object':
        df['has_projects'] = df['has_projects'].map({'true': True, 'false': False})
    if df['has_wiki'].dtype == 'object':
        df['has_wiki'] = df['has_wiki'].map({'true': True, 'false': False})
    correlation = df['has_projects'].corr(df['has_wiki'])
    return round(correlation, 3)

correlation = analyze_repo_features('repositories.csv')
print(f"Correlation coeff: {correlation}")