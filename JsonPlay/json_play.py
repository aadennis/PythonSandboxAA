import pandas as pd

df = pd.read_csv('rulers2.csv') 
# Optional: inspect the DataFrame
print(df.head())

# without this, default can display as a decimal, not an integer
df['Reign_Start'] = pd.to_numeric(df['Reign_Start'],errors='coerce').astype('Int64')
df['Reign_End'] = pd.to_numeric(df['Reign_End'],errors='coerce').astype('Int64')


print(df.head(10))

# Write the DataFrame to a JSON file
df.to_json('rulers2.json', orient='records', indent=4)