# Converting credit card transactions to Homebank format
## Input format: Nationwide (UK) CSV

Given a credit card csv file in Nationwide (UK) format, generate a csv format acceptable to Homebank.  
Nationwide excludes location data from its ofx output, hence no ofx conversion here.  
Homebank - it turns out that the [info] and [tag] fields are never exported to the QIF format. But they can be exported as the native .XHB format, so may have some value.

```get-content -Path .\(wildcard) >    
   
```e.g. get-content -Path .\*x2*csv > ./nw_all.csv  

___
The entry point for scanning and converting a directory of statements is 
```convert_nw_transactions_v2()
If you only want to convert a single statement, use ```convert_nw_to_homebank_csv_v2
