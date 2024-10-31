import pandas as pd
import statsmodels.api as sm
csv_file = '../users.csv'  
df = pd.read_csv(csv_file)
df = df[df['bio'].notnull()]
df['bio_word_count'] = df['bio'].str.split().str.len()
X = df['bio_word_count']
y = df['followers']

X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
slope = model.params['bio_word_count']
print(f"\nSlope of Regression : followers on bio word count: {slope:.3f}")