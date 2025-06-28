import pandas as pd

# Path to your data file
input_file = "data/calorie_data.csv"
output_file = "data/calorie_table.xlsx"

# Load data from CSV
df = pd.read_csv(input_file)

# Save to Excel
df.to_excel(output_file, index=False)

print(f"Calorie table saved to {output_file}")