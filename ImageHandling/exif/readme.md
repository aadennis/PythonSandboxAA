# Add subject tags to an image file

## Motivation
Neither google nor Onedrive have a simple command line way to add subject exif tags (e.g. #sport, #football, etc) to an image or batch of images.   
This script aims to fill that gap: given a file or a set of files matching some condition, add a subject exif tag to that file(s).  
If that file is in say a OneDrive folder, then you can search for all tags with a given name (again, e.g. #sport etc).  

## Dependencies
The script is a wrapper over Phil Harvey's ExifTool: https://www.exiftool.org/.  
I have not checked in the source. Right now, the version I use is 12.36.  
The latest versions are here (replace "x" with a number above 12.35):  
linux: https://www.exiftool.org/Image-ExifTool-12.x.tar.gz  
Windows: https://www.exiftool.org/exiftool-12.x.zip  

### Important!!
1. The code expects to find the working exes here:
  - PythonSandboxAA\ImageHandling\exif\src\third_party
2. The tests expect an environment variable ```EXIFTOOL="Y"```. Else the tests are skipped.

Note to self: exiftool backups are here:  
D:\software\PhotoSoftware\Exif\linux\Image-ExifTool-12.37  
D:\software\PhotoSoftware\Exif\Windows\exiftool.exe  

### ExifTool defaults
All this, AFAICT:
When you add a tag to a file, a copy is made before adding that tag. If the extension is say .jpg, then the file copy keeps the same name, but has .jpg_original as its new extension. For example:  

<img width="574" alt="image" src="https://user-images.githubusercontent.com/11707983/161144778-2cf4f6d7-bb38-4bac-a627-e3933aac50fe.png">  

In terms of performance, I found it simplest to wait until the tag updates are done, then run this:  
<img width="231" alt="image" src="https://user-images.githubusercontent.com/11707983/161145128-6ca31828-1185-4c16-9f35-da04e08c49d5.png">  

git bash seemed to hang, hence PowerShell.  

### IOS files are png...
At least, when they are moved to Windows. And png files have no tags (in the sense that I use them here, for cataloging).
The function ```GistTypes\src\convert_fileset_from_png_to_jpg.py``` handles that by converting the png to jpg. Although you could rename the png to jpg, you will find that the tag metadata slots are not available. You must run the conversion, which is done courtesy of ```Pillow```.

### OneDrive album display limits
Yes you can create a OneDrive photo album with say 1,000 photos. However, it seems it will only display 100 at a time. On a PC, anyway.
100 seems crazily limiting. Typically my albums are a month of photos, and average 700. Yes I could break them down, but I so do not want to.
Yup, it's an issue: https://techcommunity.microsoft.com/t5/onedrive-for-business/onedrive-shared-view-of-folder-limits-to-100-files/m-p/78826/page/2
