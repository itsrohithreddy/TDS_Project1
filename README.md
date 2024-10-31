# GitHub Users in the city Tokyo

This repository contains data about GitHub users in Tokyo with over 100 followers and their repositories.

## Files

1. `users.csv`: Contains information about 545 GitHub users in the city Tokyo with over 200 followers
2. `repositories.csv`: Contains information about 67157 public repositories from these users
3. `gitscrap.py`: Python script used to scrap this data from GitHub

## Data Collection

- Data collected using GitHub API
- Date of collection: 2024-10-31
- Only included users with 200 and 200+ followers
- With up to 500 most recently pushed repositories per user


## The most interesting and surprising fact

- The correlation coefficient between #public repos and followers is 0.051 ~ 0.00 indicating no linear dependence between #public repos and followers.
- The feild `email` in users.csv has the most null values(232 null values out of 545 rows) which is quite surprising. It is important to provide email so that github can stay in touch with the developer. It can send notifications at the time of creation of Personal Access Token(PAT).

## Recommendation for Developers 
- Its better to use english as the common language; developers should provide details in english.
