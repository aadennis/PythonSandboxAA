# docs:
# https://bit.ly/dw_pandas
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
# https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html


from IPython.display import display
from pprint import pprint
import pandas as pd

df = pd.read_csv('./gist_purecsv.csv')
print('--- dataframe content ---')
display(df.head())
# both display and pprint seem to display the same
pprint(df)
# or simpler!...
# df
# but nothing - possibly needs repl 

print('--- index content ---')
pprint(df.index)
print('--- columns content ---')
pprint(df.columns)
print('--- data content ---')
pprint(df.values)

print('--- index type ---')
pprint(type(df.index))
print('--- columns type ---')
pprint(type(df.columns))
print('--- data type of the df as a whole - note this is a NumPy n-dimensional array ---')
pprint(type(df.values))

print('--- data type of the individual columns (nope)---')
pprint(type(df.dtypes))
df.dtypes
pprint(df.info)

a = df["Transactions"].str.capitalize()
pprint(a.info)

