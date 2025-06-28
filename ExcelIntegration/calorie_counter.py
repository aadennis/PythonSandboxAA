import pandas as pd

# Define the updated calorie data
data = {
    "Food Item": [
        "Frozen Strawberries", "Frozen Bananas", "Greek Yoghurt (plain, non-fat)",
        "Brown Sugar (1 tbsp)", "Brown Sugar (1 tsp)", "Semi-skimmed Milk (50 ml)",
        "Semi-skimmed Milk (100 ml)", "Sourdough Bread", "Butter", "Jam", "Honey",
        "Homemade Vegetable Soup", "Full-Fat Milk", "Peas", "Lidl Greek Style Yoghurt (Full Fat)"
    ],
    "Calories (kcal)": [
        32, 89, 59, 52, 17, 25, 50, 174, 102, 56, 64, 100, 64, 81, 126
    ],
    "Amount": [
        100, 100, 100, 1, 1, 50, 100, 1, 1, 1, 1, 1, 200, 100, 100
    ],
    "Unit": [
        "g", "g", "g", "tbsp", "tsp", "ml", "ml", "slice", "tbsp", "tbsp", "tbsp", "bowl", "ml", "g", "g"
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "calorie_table.xlsx"
df.to_excel(output_file, index=False)

print(f"Calorie table saved to {output_file}")