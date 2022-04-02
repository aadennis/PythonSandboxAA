# Consolidate OneDrive photos into a single folder

## Motivation and Problem
-  OneDrive uses many folders to store pictures
## Solution
-  As a OneDrive user
-  I want all pictures taken (photos, screenshots, movies) consolidated into a single folder
-  So that from that folder, I can assign pictures to appropriate albums
## Detail
The onedrive/Pictures folder contains 7 named sub-folders, a set dictated by Microsoft. 
This consolidates any content from those folders (and sub-sub-etc-folders), to a single, randomly named flat folder.  
It is then up to the user to move, by hand, those files to the appropriate folder.  
For me "appropriate" is, in the first instance, month and year.  
If the files are mostly from October 2021, for example, then the appropriate folder would likely be D:/onedrive/stuff/CRD_2021_10. That is just based on my setup.
You might be expecting automation to take of distributing the files in the bucket to the appropriate year-month folder. 
However it is easiest to sort by date descending, review, and move each year-month batch to the right folder. For Windows at least, OneDrive will recognise 
that they are being moved, and not complain about many files being deleted.
