import csv
from collections import Counter

languages = []

with open('repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row.get('language', '').strip()
        if language:
            languages.append(language)

language_counts = Counter(languages)
most_common_language = language_counts.most_common(1)

if most_common_language:
    print(most_common_language[0][0])
else:
    print("No language data found.")
