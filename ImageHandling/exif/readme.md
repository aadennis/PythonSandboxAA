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

Note to self: exiftool backups are here:
D:\software\PhotoSoftware\Exif\linux\Image-ExifTool-12.37
D:\software\PhotoSoftware\Exif\Windows\exiftool.exe

