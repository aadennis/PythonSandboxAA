import pandas as pd

df = pd.read_csv('rulers2.csv')

# Optional: inspect the DataFrame
print(df.head())

# Write the DataFrame to a JSON file
df.to_json('rulers2.json', orient='records', indent=4)