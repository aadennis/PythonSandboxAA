import pandas as pd
import re
from pathlib import Path

# Use relative path for data I/O
input_file = Path("data/calorie_data.csv")
output_file = Path("data/calorie_table_with_codes.xlsx")

# Load data from CSV
df = pd.read_csv(input_file)

# Helper function to generate base code
def make_base_code(name):
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', name).upper().split()
    if not cleaned:
        return "XXXX"
    if len(cleaned) == 1:
        return (cleaned[0][:4] + "XXXX")[:4]
    return "".join(word[0] for word in cleaned[:4]).ljust(4, "X")

# Generate unique 4-char codes
code_counts = {}
codes = []

for item in df["Food Item"]:
    base = make_base_code(item)
    count = code_counts.get(base, 0)
    code = f"{base[:3]}{count + 1}" if count else base
    code_counts[base] = count + 1
    codes.append(code)

# Insert the Code column after Food Item
df.insert(1, "Code", codes)

# Save straight to Excel
df.to_excel(output_file, index=False)

print(f"Data with unique codes exported to Excel: {output_file}")