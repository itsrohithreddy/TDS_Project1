import csv
users_in_tokyo = []

with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        if 'tokyo' in location:
            users_in_tokyo.append({
                'login': row['login'],
                'followers': int(row['followers'])
            })

top_users = sorted(users_in_tokyo, key=lambda x: x['followers'], reverse=True)
top_5_logins = [user['login'] for user in top_users[:5]]
print(','.join(top_5_logins))