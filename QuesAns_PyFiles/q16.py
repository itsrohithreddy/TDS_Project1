import csv
from collections import Counter
surname_counter = Counter()

with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        name = row.get('name', '').strip()
        if name:
            surname = name.split()[-1]
            surname_counter[surname] += 1

if surname_counter:
    max_count = max(surname_counter.values())
    most_common_surnames = [surname for surname, count in surname_counter.items() if count == max_count]
    most_common_surnames.sort()
    print(f"{', '.join(most_common_surnames)}: {max_count}")
else:
    print("No names found.")
