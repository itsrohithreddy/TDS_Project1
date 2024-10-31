import pandas as pd

def analyze_email_sharing(users_csv_path='../users.csv'):
    df = pd.read_csv(users_csv_path)
    df['has_email'] = df['email'].notna() & (df['email'] != '')
    
    hireable_mask = df['hireable'] == True
    if hireable_mask.any():
        hireable_email_fraction = df[hireable_mask]['has_email'].mean()
    else:
        hireable_email_fraction = 0
        
    non_hireable_mask = df['hireable'] != True
    if non_hireable_mask.any():
        non_hireable_email_fraction = df[non_hireable_mask]['has_email'].mean()
    else:
        non_hireable_email_fraction = 0
    
    difference = round(hireable_email_fraction - non_hireable_email_fraction, 3)
    return difference

result = analyze_email_sharing()
print(f"\nresult: {result:.3f}")