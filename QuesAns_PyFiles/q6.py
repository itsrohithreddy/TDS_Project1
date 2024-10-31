import csv
from collections import Counter
from datetime import datetime

languages = []
joindate = dict()
with open('../users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        joindate[row.get('login')] = row.get('created_at')

with open('../repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        created_at = joindate.get(row.get('login'))
        if created_at:
            user_join_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
            if user_join_date.year >= 2020:
                language = row.get('language', '').strip()
                if language:
                    languages.append(language)
language_counts = Counter(languages)
most_common_languages = language_counts.most_common(2)
if len(most_common_languages) >= 2:
    print(most_common_languages[1][0])
else:
    print("Not enough language data found.")
