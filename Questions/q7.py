import csv
from collections import defaultdict

language_stats = defaultdict(lambda: {'stars': 0, 'repos': 0})

with open('repositories.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        language = row.get('language', '').strip()
        stars = row.get('stargazers_count', '0').strip()
        if language and stars.isdigit():
            language_stats[language]['stars'] += int(stars)
            language_stats[language]['repos'] += 1

average_stars_per_language = {
    language: stats['stars'] / stats['repos']
    for language, stats in language_stats.items()
    if stats['repos'] > 0
}

if average_stars_per_language:
    most_popular_language = max(average_stars_per_language, key=average_stars_per_language.get)
    print(most_popular_language)
else:
    print("No language data found.")
