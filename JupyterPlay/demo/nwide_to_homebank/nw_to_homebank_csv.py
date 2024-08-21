
# Given a credit card csv file in Nationwide (UK) format,
# generate a csv format acceptable to Homebank.
# Nationwide excludes location data from its ofx output,
# hence no ofx conversion here.
# Homebank - it turns out that the [info] and [tag] fields are never 
# exported to the QIF format. But they can be exported
# as the native .XHB format, so may have some value.
# Given the total absence of good practice here, there are 
# many todos.

# include these in requirements.txt:
import pandas as pd
import pprint
import glob
import os
import configparser
from datetime import datetime

def create_config():
    config = configparser.ConfigParser()
    config['General'] = {'debug': True, 'log_level': 'info'}
    config['Database'] = {'db_name': 'example_db', 'db_host': 'localhost', 'db_port': '5432'}
    config['TransactionConfig'] = {'cc_txn_source_path': r'nonsense', 'x': '22', 'y': '44'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_config():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    cc_txn_source_path = config.get('TransactionConfig', 'cc_txn_source_path')

    config_values = {
        'cc_txn_source_path': cc_txn_source_path
    }
    return config_values

def convert_nw_to_homebank_csv(in_file, out_file):
    # First, get the file content into a df. 
    # Keep the header row from the input file, in order to match
    # input (source bank) and output (Homebank required format) 
    # columns correctly.
    # Note the encoding as delivered by Nationwide
    nw_encoding = 'cp1252'
    input_df = pd.read_csv(in_file, skiprows=4, encoding=nw_encoding)

    #perform basic data manipulation
    output_df = pd.DataFrame({
        "Date": pd.to_datetime(input_df["Date"], format="%d %b %Y"),
        "payment type": 1,  # placeholder
        "info": "info 1",  # placeholder
        "Transactions": input_df["Transactions"],
        "Location": input_df["Location"],
        "Paid out": input_df["Paid out"].astype(str).str.replace("£", ""),
        "Paid in": input_df["Paid in"].astype(str).str.replace("£", ""),
        "category": "category 1",  # placeholder
        "Tags": "tag1 tag2"  # placeholder
    })
    
    # Do the more complex stuff in a second pass
    # When looking through Homebank transactions, it is useful to know where
    # one statement ends, and another starts
    output_df.loc[0,'info'] = 'First transaction in statement'
    output_df.loc[output_df.index[-1],'info'] = 'Last transaction in statement'
    
    output_df.fillna(0,inplace=True)
    output_df["Paid out"] = output_df["Paid out"].astype(float)
    output_df["Paid in"] = output_df["Paid in"].astype(float)
    output_df["Paid"] = output_df.apply(lambda row: (row["Paid out"] * -1) if row["Paid out"] > 0.0 else row["Paid in"], axis = 1)
    
    # Finally in a form that HomeBank can ingest:
    columns_to_delete = ["Paid out", "Paid in"] 
    output_df.drop(columns=columns_to_delete, inplace=True)
    desired_order = [0,1,2,3,4,7,5,6]
    output_df = output_df.iloc[:, desired_order]
    
    pprint.pprint(output_df) # debug
    
    output_df.to_csv(out_file, sep=";", index=False, header=False)

def convert_nw_transactions():
    config_data = read_config()
    in_dir = config_data['cc_txn_source_path']
    for f in glob.iglob(f'{in_dir}/*Statement Download*.csv'):
        print(f)
        file_name = os.path.basename(f)
        out_file=f'{in_dir}/{file_name[0:2]}_outputx.csv'
        print(out_file)
        convert_nw_to_homebank_csv(f, out_file)

convert_nw_transactions()

#create_config()

