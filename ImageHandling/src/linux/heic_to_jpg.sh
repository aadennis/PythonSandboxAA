# WARNING: Make a backup copy of all your images before running this code.
extension=HEIC
pwd
image_file_dir=../../tests/images
cd $image_file_dir
echo "adsfafff"
pwd
for inFile in `ls *.${extension}`
do
    baseFilename=`basename $inFile .${extension}`
    outFile="${baseFilename}.jpg"
    echo "$inFile --> $outFile"
    magick $inFile $outFile
    #mogrify -resize 50% $outFile   # Resize the image to 50% of the original size
done
