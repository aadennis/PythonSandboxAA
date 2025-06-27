'''
 Convert a Markdown file with vocabulary tables into an Excel file with multiple sheets.
 See welsh_vocab_builder.md for the expected format.
'''
import pandas as pd
import re

# Load the Markdown file content
file_path = "data/welsh_vocab_builder.md"
with open(file_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Use regex to split sections by headings (##) and extract title + table
sections = re.split(r"(## .+?)\n\n+", md_content)

# Dictionary to hold section title and parsed table DataFrames
section_tables = {}

# Parse each section
for i in range(1, len(sections), 2):
    section_title = re.sub(r"[^\w\s]", "", sections[i].strip())  # clean title for sheet name
    raw_table = sections[i+1].strip()

    # Skip non-table content
    if '|' not in raw_table:
        continue

    # Remove MD separator lines like |----|----|
    lines = [line for line in raw_table.splitlines() if not re.match(r"^\|[-\s|]+\|?$", line.strip())]

    if len(lines) < 2:
        continue

    headers = [h.strip() for h in lines[0].strip('|').split('|')]
    data = [
        [cell.strip() for cell in line.strip('|').split('|')]
        for line in lines[1:]
    ]

    # Create DataFrame
    df = pd.DataFrame(data, columns=headers)
    sheet_name = section_title[:31]  # Excel sheet name limit
    section_tables[sheet_name] = df

# Save to Excel with one sheet per section
output_excel_path = "data/welsh_vocab_builder.xlsx"
with pd.ExcelWriter(output_excel_path, engine='xlsxwriter') as writer:
    for sheet_name, df in section_tables.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

output_excel_path
