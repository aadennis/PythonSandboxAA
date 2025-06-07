# pip install pdfplumber pandas
import pdfplumber
import pandas as pd
import re

def extract_nationwide_txns(filepath, csv_output_path="nationwide_txns.csv"):
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
        if line.lower().startswith("balance from previous"):
            continue

        m = re.match(
            r"(?P<date>\d{2}/\d{2}/\d{2})\s+"
            r"(?:(?P<ref>\d+)\s+)?"
            r"(?P<desc>.+?)\s+"
            r"£(?P<amount>[\d,]+\.\d{2})(?P<cr>CR)?",
            line.strip()
        )

        if m:
            groups = m.groupdict()
            amount = float(groups['amount'].replace(",", ""))
            signed_amount = amount if groups['cr'] else -amount

            data_rows.append({
                "txn_date": groups['date'],
                "reference": groups['ref'] or "",
                "description": groups['desc'].strip(),
                "amount": signed_amount
            })
        else:
            print(f"Skipped line (unmatched): {line}")

    df = pd.DataFrame(data_rows)
    
    # Export to CSV
    df.to_csv(csv_output_path, index=False)
    print(f"\n✅ Transactions saved to: {csv_output_path}")

    return df

# Example usage



df = extract_nationwide_txns("C:/temp/mark/mark.pdf")
print(df)


