"""
nw_to_homebank_csv_v2b.py

This module converts credit card transactions to Homebank format
Input format: Nationwide (UK) CSV

Given a credit card csv file in Nationwide (UK) format, generate a csv format acceptable to Homebank.  
This script expects (Nationwide) csv data as input.
OFX files are not supported here, as Nationwide excludes location data from its ofx output.
Homebank - it turns out that the [info] and [tag] fields are never exported to the QIF format. 
But they can be exported as the native .XHB format, so may have some value.
"""

# include pandas in requirements.txt:
import pandas as pd
from pprint import pprint
import glob
import os

from utility import read_env_var

def convert_nw_to_homebank_csv(in_file, out_file):
    """
    Get the file content into a df.
         - Note the encoding as delivered by Nationwide.
     - Do basic data manipulation  
         - Keep the header row from the input file, in order to match  input (source bank) and output (Homebank required format) columns correctly
     - More complex processing
         -  Record location of first and last statements in a transaction. This is useful to separate one statement from another, visually
         -  Position the df columns as expected by HomeBank
     - Write a HomeBank-compliant file back out
    """

    nw_encoding = 'cp1252'
    input_df = pd.read_csv(in_file, skiprows=4, encoding=nw_encoding)

    # perform basic data manipulation
    output_df = pd.DataFrame({
        "Date": pd.to_datetime(input_df["Date"], format="%d %b %Y"),
        "payment type": 1,  # placeholder
        "info": "info 1",  # placeholder
        "Transactions": input_df["Transactions"].str.capitalize(),
        "Location": input_df["Location"],
        "Paid out": input_df["Paid out"].astype(str).str.replace("£", ""),
        "Paid in": input_df["Paid in"].astype(str).str.replace("£", ""),
        "category": "category 1",  # placeholder
        "Tags": "tag1 tag2"  # placeholder
    })

    output_df.loc[0, 'info'] = 'First transaction in statement'
    output_df.loc[output_df.index[-1],
                  'info'] = 'Last transaction in statement'
    output_df = format_paid_columns(output_df)

    desired_order = [0, 1, 2, 3, 4, 7, 5, 6]
    output_df = output_df.iloc[:, desired_order]

    pprint(output_df)  # debug
    output_df.to_csv(out_file, sep=";", index=False, header=False)


# Values in the Paid out and Paid in columns are mutually exclusive.  
# Write the not-null value to a Paid column, and drop the original columns.

def format_paid_columns(df):
    df.fillna(0, inplace=True)
    df["Paid out"] = df["Paid out"].astype(float)
    df["Paid in"] = df["Paid in"].astype(float)
    df["Paid"] = df.apply(lambda row: (row["Paid out"] * -1)
                           if row["Paid out"] > 0.0 else row["Paid in"], axis=1)
    # original Paid columns can now be dropped
    columns_to_delete = ["Paid out", "Paid in"]
    df.drop(columns=columns_to_delete, inplace=True)

    pprint(df)
    return df

def read_nw_csv(file_path, encoding='CP1252'):
    """Reads the Nationwide CSV file and returns a DataFrame."""
    print(pd.__version__)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    return pd.read_csv(file_path, skiprows=4, encoding=encoding)


def preprocess_data(input_df):
    """Performs basic data manipulation on the input DataFrame."""
    output_df = pd.DataFrame({
        "Date": pd.to_datetime(input_df["Date"], format="%d %b %Y"),
        "payment type": 1,  # placeholder
        "info": "info 1",  # placeholder
        "Transactions": input_df["Transactions"].str.capitalize(),
        "Location": input_df["Location"],
        "Paid out": input_df["Paid out"].astype(str).str.replace("£", ""),
        "Paid in": input_df["Paid in"].astype(str).str.replace("£", ""),
        "category": "category 1",  # placeholder
        "Tags": "tag1 tag2"  # placeholder
    })
    return output_df


def add_transaction_info(output_df):
    """Adds transaction info to the output DataFrame."""
    output_df.loc[0, 'info'] = 'First transaction in statement'
    output_df.loc[output_df.index[-1],
                  'info'] = 'Last transaction in statement'
    return output_df


def reorder_columns(output_df):
    """Reorders columns in the output DataFrame."""
    desired_order = [0, 1, 2, 3, 4, 7, 5, 6]
    return output_df.iloc[:, desired_order]


def convert_nw_to_homebank_csv(in_file, out_file) -> pd.DataFrame:
    input_df = read_nw_csv(in_file)
    output_df = preprocess_data(input_df)
    output_df = add_transaction_info(output_df)
    output_df = format_paid_columns(output_df)
    output_df = handle_special_payees(output_df)
    output_df = reorder_columns(output_df)
    output_df.to_csv(out_file, sep=";", index=False, header=False)
    return output_df

# Resolve the passed path and wildcard. It must resolve to a single
# file. Anymore than that throws an exception.
# Then proceed with the conversion to the HomeBank format.
def convert_nw_transactions(in_dir, nw_csv_file) -> pd.DataFrame:
    file_path = f'{in_dir}/{nw_csv_file}'
  
    matching_files = list(glob.iglob(file_path))
    if len(matching_files) > 1:
        raise Exception("More than one matching file found")    

    if len(matching_files) == 0:
        raise FileNotFoundError("No matching file found")

    f = matching_files[0]
    file_name = os.path.basename(f)
    out_file = f'{in_dir}/{file_name[0:2]}_outputx.csv'

    return convert_nw_to_homebank_csv(f, out_file)

def handle_special_payees(df):
    # Some frequent payees have sub-divisions which categorize
    # them, once you know the pattern... which is quite simple,
    # frequently

    df['Transactions'] = df['Transactions'].apply(
        # Amazon and its variants
        lambda x: 'Amazon' if x.startswith('Amazon') or x.startswith('Amzn') or x.startswith('Www.amazon') else x)
    # Flag Direct Debit Payment as Category 11 for Homebank purposes
    df['payment type'] = df['Transactions'].apply(
        lambda x: '11' if x.upper().startswith('DIRECT DEBIT PAYMENT') else '1')
    return df


# Entry point / Example usage:
if __name__ == "__main__":
    cc_txn_source_path = read_env_var('cc_txn_source_path')
    csv_file = '16 Statement Download*.csv'
    a = convert_nw_transactions(cc_txn_source_path, csv_file)
    a.head()
   




