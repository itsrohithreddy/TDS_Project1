import csv
from datetime import datetime
users_in_tokyo = []

with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        if 'tokyo' in location:
            users_in_tokyo.append({
                'login': row['login'],
                'created_at': datetime.strptime(row['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            })


sorted_users = sorted(users_in_tokyo, key=lambda x: x['created_at'])
top_5_earliest_logins = [user['login'] for user in sorted_users[:5]]
print(','.join(top_5_earliest_logins))
