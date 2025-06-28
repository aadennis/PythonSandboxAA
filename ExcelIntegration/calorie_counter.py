import pandas as pd
import re
from pathlib import Path

# File paths
input_file = Path("data/calorie_data.csv")
output_file = Path("data/calorie_table_with_codes.xlsx")

# Load data
df = pd.read_csv(input_file)

# Generate base codes
def make_base_code(name):
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', name).upper().split()
    if not cleaned:
        return "XXXX"
    if len(cleaned) == 1:
        return (cleaned[0][:4] + "XXXX")[:4]
    return "".join(word[0] for word in cleaned[:4]).ljust(4, "X")

# Create unique codes
code_counts = {}
codes = []

for item in df["Food Item"]:
    base = make_base_code(item)
    count = code_counts.get(base, 0)
    code = f"{base[:3]}{count + 1}" if count else base
    code_counts[base] = count + 1
    codes.append(code)

# Reorder and insert Code column
df.insert(1, "Code", codes)
df = df[["Food Item", "Code", "Amount", "Unit", "Calories (kcal)"]]

# Export to Excel with autofit
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Food Items", index=False)
    
    # Autofit columns
    workbook = writer.book
    worksheet = writer.sheets["Food Items"]
    
    for i, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(i, i, max_len)

print(f"Excel file with autofit columns saved to: {output_file}")

