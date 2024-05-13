#!/bin/zsh

# WARNING: Make a backup copy of all your images before running this code.
# Make a copy of all .heic files in the given folder, in .jpg format
# usage: bash ./heic_to_jpg.sh

# Source the config file
source config.cfg

extension=HEIC
pwd
cd $image_file_dir
echo "Current folder..."
pwd
shopt -s nocaseglob  # Enable case-insensitive filename expansion
for inFile in `ls *.${extension}`
do
    baseFilename=`basename $inFile .${extension}`
    outFile="${baseFilename}.jpg"
    echo "Converting [$inFile] --> [$outFile]"
    magick $inFile $outFile
done
