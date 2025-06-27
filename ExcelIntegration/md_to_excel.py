import pandas as pd

def md_pipe_to_excel(md_file, excel_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Filter out separator lines (like |----|----|)
    data_lines = [line.strip() for line in lines if line.strip() and not all(c in '-| ' for c in line)]

    # Parse lines into list of lists, splitting by pipe, stripping spaces
    table = []
    for line in data_lines:
        # Remove starting and ending pipe if present, then split by '|'
        row = [cell.strip() for cell in line.strip('|').split('|')]
        table.append(row)

    # Create DataFrame from table
    df = pd.DataFrame(table[1:], columns=table[0])  # first row = headers

    # Save to Excel
    df.to_excel(excel_file, index=False)
    print(f"Converted '{md_file}' to '{excel_file}' successfully.")

# Example usage:
md_pipe_to_excel('data/welsh_vocab_builder.md', 'output.xlsx')
