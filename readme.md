# Consolidate OneDrive photos into a single folder

## Motivation and Problem
-  OneDrive uses many folders to store pictures
## Solution
-  As a OneDrive user
-  I want all pictures taken (photos, screenshots, movies) consolidated into a single folder
-  So that from that folder, I can assign pictures to  appropriate albums
### Detail
The onedrive/Pictures folder contains 7 named sub-folders, a set dictated by Microsoft. 
This consolidates any content from those folders (and sub-sub-etc-folders), to a single, randomly named flat folder.  
It is then up to the user to move, by hand, those files to an appropriate folder.  
For me, "appropriate" is, in the first instance, month and year.  
If the files are mostly from October 2021, for example, then the appropriate folder would likely be ```D:/onedrive/stuff/CRD_2021_10.```  That is just based on my setup.
You might be expecting automation to take of distributing the files in the bucket to the appropriate year-month folder. 
However, I find it is safest to sort by date descending, review, and move each year-month batch to the right folder. For Windows at least, OneDrive will recognise 
that they are being moved, and not complain about many files being deleted.

## Usage
### Dependencies
1. Checkout this repo  
1. Python3  
1. Windows (not tested under linux)  
``` cd (git repo root)  ```  
``` cd PythonSandboxAA/FileHandling/src  ```

Example 1: this will read a root_folder "D:/onedrive/Pictures" and move all files found, including in subfolders, to the single folder = "D:/onedrive/stuff/Bucketx", 
where "Bucketx" is a generated random name  
```py FileHandling.py ```  

Example 2: this will read a root_folder "D:/onedrive/MyPictures" and move all files found, including in subfolders, to the single folder = "e:/mybackupx/Bucketx".   Note that changing the folder to e: etc is dangerous, because OneDrive will record a deletion, not a move.  
If you pass the source or destination, they must be full paths.  
```
src_folder = "D:/onedrive/MyPictures"  
dest_folder = "e:/mybackupx"  
py FileHandling.py -s src_folder -d dest_folder
```  
