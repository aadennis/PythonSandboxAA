# Converting credit card transactions to Homebank format
## Input format: Nationwide (UK) CSV

Given a credit card csv file in Nationwide (UK) format, generate a csv format acceptable to Homebank.  
Nationwide excludes location data from its ofx output, hence no ofx conversion here.  
Homebank - it turns out that the [info] and [tag] fields are never exported to the QIF format. But they can obviouisly be saved in their native format of .XHB, so may have some value.

`get-content -Path .\(wildcard) >    `  
e.g.   
`get-content -Path .\*x2*csv > ./nw_all.csv  `


___
The entry point for scanning and converting a directory of statements is   
`convert_nw_transactions_v2()`  

If you only want to convert a single statement, use   `convert_nw_to_homebank_csv_v2`

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