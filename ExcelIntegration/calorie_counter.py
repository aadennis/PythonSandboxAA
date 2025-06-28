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
    fooditem_sheet = writer.sheets["Food Items"]
    
    for i, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
        fooditem_sheet.set_column(i, i, max_len)

    # --- Write Meals Sheet ---
    meals_sheet = workbook.add_worksheet("Meals")
    writer.sheets["Meals"] = meals_sheet

    # Format definitions
    bold = workbook.add_format({"bold": True})
    header = workbook.add_format({"bold": True, "font_size": 14})
    subhead = workbook.add_format({"bold": True, "font_size": 12})
    num_fmt = workbook.add_format({"num_format": "0.0"})

    # Meal definition
    meal_def = {
        "FSXX": 1,
        "FBXX": 1,
        "LGSY": 1,
        "BS1T": 1,
        "SM1M": 1.5,
        "HONE": 1
    }
    meal_name = "Breakfast"

    # Lookup and build meal content
    lookup_df = df.set_index("Code")[["Food Item", "Calories (kcal)"]]
    meal_rows, total_kcal = [], 0

    for code, count in meal_def.items():
        item = lookup_df.loc[code, "Food Item"] if code in lookup_df.index else "Not Found"
        kcal = lookup_df.loc[code, "Calories (kcal)"] if code in lookup_df.index else 0
        total = kcal * count
        total_kcal += total
        meal_rows.append([code, item, count, kcal, total])

    # Write content
    meals_sheet.write("A1", "Meals", header)
    meals_sheet.write("A3", meal_name, subhead)
    headers = ["Code", "Food Item", "Count", "Calories per Unit", "Total Calories"]
    for col, title in enumerate(headers):
        meals_sheet.write(4, col, title, bold)

    for row, data in enumerate(meal_rows, start=5):
        for col, val in enumerate(data):
            fmt = num_fmt if isinstance(val, float) else None
            meals_sheet.write(row, col, val, fmt)

    # Write total calories
    meals_sheet.write(row + 2, 3, "Total:", bold)
    meals_sheet.write(row + 2, 4, total_kcal, num_fmt)        

print(f"Excel file with autofit columns saved to: {output_file}")

