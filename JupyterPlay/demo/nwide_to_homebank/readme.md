# Converting credit card transactions to Homebank format
## Input format: Nationwide (UK) CSV

Given a credit card csv file in Nationwide (UK) format, generate a csv format acceptable to Homebank.  
Nationwide excludes location data from its ofx output, hence no ofx conversion here.  
Homebank - it turns out that the [info] and [tag] fields are never exported to the QIF format. But they can obviouisly be saved in their native format of .XHB, so may have some value.

### Module name:  
`nw_to_homebank_csv.py`

### The entry point for scanning and converting a directory of statements
`convert_nw_transactions_v2()`  

This reads `utility.read_config` to determine a) the input folder, and b) the location of the file which concatenates the output from the multiple statements.
This calls `convert_nw_to_homebank_csv_v2()` (see below), multiple times. In fact, as many times as there are statements in the input folder.

### If you only want to convert a single statement, use  
`convert_nw_to_homebank_csv_v2(input file, output file)`

A number of functions support that top-level call. (#todo Mermaid)

`convert_nw_to_homebank_csv`
- Get the file content into a df.
    - Note the encoding as delivered by Nationwide.
- Do basic data manipulation  
    - Keep the header row from the input file, in order to match  input (source bank) and output (Homebank required format) columns correctly
- More complex processing
    -  Record location of first and last statements in a transaction. This is useful to separate one statement from another, visually
    -  Position the df columns as expected by HomeBank
- Write a HomeBank-compliant file back out