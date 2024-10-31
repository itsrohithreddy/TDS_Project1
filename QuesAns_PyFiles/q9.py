import csv
import numpy as np

followers = []
public_repos = []

with open('../users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        location = row.get('location', '').strip().lower()
        if "tokyo" in location:
            try:
                followers_count = int(row['followers'])
                public_repos_count = int(row['public_repos'])
                followers.append(followers_count)
                public_repos.append(public_repos_count)
            except ValueError:
                print("Error")
                continue

if len(followers) > 1 and len(public_repos) > 1:
    correlation_matrix = np.corrcoef(followers, public_repos)
    correlation = correlation_matrix[0, 1]
    print(f"{correlation:.3f}")
else:
    print("Insufficient data for correlation calculation.")
