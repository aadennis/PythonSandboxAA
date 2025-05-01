# pip install pdfplumber pandas

import pdfplumber
import pandas as pd
import re

def extract_nationwide_txns(filepath):
    with pdfplumber.open(filepath) as pdf:
        full_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    # Narrow to relevant section
    pattern = r"Balance from previous statement.*?(?=TOTAL BALANCE)"
    match = re.search(pattern, full_text, re.DOTALL)
    if not match:
        raise ValueError("Couldn't find transaction section.")

    txn_block = match.group(0)

    lines = txn_block.strip().split("\n")
    data_rows = []

    for line in lines:
        # Skip header line
        if line.lower().startswith("balance from previous"):
            continue

        # Extract components
        m = re.match(r"(\d{2}/\d{2}/\d{2})\s+(\d+)\s+(.+?)\s+£([\d,.]+)", line)
        if m:
            txn_date, reference, description, amount = m.groups()
            data_rows.append({
                "txn_date": txn_date,
                "reference": reference,
                "description": description.strip(),
                "amount": float(amount.replace(",", ""))
            })

    return pd.DataFrame(data_rows)

# Example usage

df = extract_nationwide_txns("C:/temp/mark/mark.pdf")
print(df.head(100))


