import pandas as pd
import json

def safe_value(row, key):
    val = row.get(key)
    return "null" if pd.isna(val) else val

# Load the Excel file
df = pd.read_excel("chords.xlsx", header=0)

# Initialize output list
chords = []

# Iterate through each row
for _, row in df.iterrows():
    chord = {
        "chord_id": row["chord_id"],
        "name": safe_value(row, "name"),
        "comments": safe_value(row, "comments"),
        "tested": safe_value(row, "tested"),
        "sa_notes": []
    }
    
    # Iterate through key columns (assumes columns C to F are all labeled "key")
    for col in df.columns[4:]:
        note = row[col]
        if pd.notna(note):
            chord["sa_notes"].append({"sa_note": note})

    chords.append(chord)

# Write to JSON
with open("chords2.json", "w") as f:
    json.dump(chords, f, indent=4)
