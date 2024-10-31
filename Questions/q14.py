import csv
from collections import Counter
from datetime import datetime
weekend_repo_counts = Counter()

with open('repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        created_at = row.get('created_at', '')
        if created_at:
            created_date = datetime.fromisoformat(created_at[:-1])  # Remove 'Z' and convert
            if created_date.weekday() in [5, 6]:
                user_login = row['login']
                weekend_repo_counts[user_login] += 1
top_users = weekend_repo_counts.most_common(5)
top_logins = [user[0] for user in top_users]
print(','.join(top_logins))