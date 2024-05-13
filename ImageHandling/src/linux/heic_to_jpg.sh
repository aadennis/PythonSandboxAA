#!/bin/zsh

# WARNING: Make a backup copy of all your images before running this code.
# Make a copy of all .heic files in the given folder, in .jpg format.
# Example: if a source file is [football.heic], 
#          the target file is [football.heic.jpg]

# usage: bash ./heic_to_jpg.sh
#------------------------------------------------------------
source config.cfg

cd $image_file_dir
echo "Current folder..."
pwd
shopt -s nocaseglob  # Enable case-insensitive filename expansion
for inFile in `ls *.HEIC`
do
    baseFilename=`basename $inFile .HEIC`
    outFile="${baseFilename}.jpg"
    echo "Converting [$inFile] --> [$outFile]"
    magick $inFile $outFile
done
