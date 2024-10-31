import pandas as pd

def analyze_following_difference(users_csv_path='../users.csv'):
    df = pd.read_csv(users_csv_path)
    hireable_following = df[df['hireable'] == True]['following'].mean()
    non_hireable_following = df[df['hireable'] != True]['following'].mean()
    difference = round(hireable_following - non_hireable_following, 3)
    return difference
result = analyze_following_difference()
print(f"\nDifference in average following: {result:.3f}")