import pandas as pd
import re
import json
from pathlib import Path

# data paths in and out
# in 
with open("data/meals.json", "r") as f:
    meals = json.load(f)
with open("data/food_items.json", "r") as f:
    food_data = json.load(f)
# out    
output_file = Path("data/calorie_table_with_codes.xlsx")    

# Generate base codes
def make_base_code(name):
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', name).upper().split()
    if not cleaned:
        return "XXXX"
    if len(cleaned) == 1:
        return (cleaned[0][:4] + "XXXX")[:4]
    return "".join(word[0] for word in cleaned[:4]).ljust(4, "X")

# debug: print base codes
for item in food_data:
    name = item["Food Item"]
    print(f"{name:<45} → {make_base_code(name)}")

# Create unique codes
code_counts = {}
codes = []

df = pd.DataFrame(food_data)

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

    # Formatting
    bold = workbook.add_format({"bold": True})
    header = workbook.add_format({"bold": True, "font_size": 14})
    subhead = workbook.add_format({"bold": True, "font_size": 12})
    num_fmt = workbook.add_format({"num_format": "0.0"})

    # Lookup for food names and kcals
    lookup_df = df.set_index("Code")[["Food Item", "Calories (kcal)"]]

    # Start writing
    current_row = 0
    meals_sheet.write(current_row, 0, "Meals", header)
    current_row += 2  # spacing after header

    for meal_name, meal_def in meals.items():
        meals_sheet.write(current_row, 0, meal_name, subhead)
        current_row += 1

        headers = ["Code", "Food Item", "Count", "Calories per Unit", "Total Calories"]
        for col, title in enumerate(headers):
            meals_sheet.write(current_row, col, title, bold)
        current_row += 1

        meal_total = 0
        for code, count in meal_def.items():
            item = lookup_df.loc[code, "Food Item"] if code in lookup_df.index else "Not Found"
            kcal = lookup_df.loc[code, "Calories (kcal)"] if code in lookup_df.index else 0
            total = kcal * count
            meal_total += total
            row_data = [code, item, count, kcal, total]

            for col, val in enumerate(row_data):
                fmt = num_fmt if isinstance(val, float) else None
                meals_sheet.write(current_row, col, val, fmt)
            current_row += 1

        # Total per meal
        meals_sheet.write(current_row + 1, 3, "Total:", bold)
        meals_sheet.write(current_row + 1, 4, meal_total, num_fmt)
        current_row += 3  # spacing before next meal