# pip install pdfplumber pandas

import pdfplumber
import pandas as pd

def extract_nationwide_creditcard_pdf(filepath):
    all_data = []

    with pdfplumber.open(filepath) as pdf:
        for i, page in enumerate(pdf.pages):
            print(f"--- Page {i+1} ---")
            print(page.extract_text())

        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    # Skip header-like or empty rows
                    if row and all(cell is not None for cell in row):
                        all_data.append(row)

    # Get the most common number of columns
    col_counts = [len(row) for row in all_data]
    most_common_len = max(set(col_counts), key=col_counts.count)
    filtered_data = [row for row in all_data if len(row) == most_common_len]

    # Assign default column names
    default_columns = [f"Col{i+1}" for i in range(most_common_len)]
    df = pd.DataFrame(filtered_data, columns=default_columns)

    return df

# Example usage


df = extract_nationwide_creditcard_pdf("C:/temp/mark/mark.pdf")
print(df.head())


# with pdfplumber.open(filepath) as pdf:
#     for i, page in enumerate(pdf.pages):
#         print(f"--- Page {i+1} ---")
#         print(page.extract_text())
