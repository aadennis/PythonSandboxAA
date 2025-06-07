#!/bin/bash

# Input AVI file
INPUT_AVI="$1"
if [ -z "$INPUT_AVI" ]; then
    echo "Usage: $0 <input.avi>"
    exit 1
fi

# Extract metadata
FILENAME=$(basename "$INPUT_AVI")
DURATION=$(ffprobe -v error -select_streams v:0 -show_entries format=duration -of default=noprint_wrappers=1 "$INPUT_AVI")
DATE_CREATED=$(stat -c %y "$INPUT_AVI" | cut -d' ' -f1)  # Linux stat command

# Generate credits image
magick convert -size 1280x720 xc:black -fill white -gravity center \
    -pointsize 32 -annotate +0+0 "Filename: $FILENAME\nDate: $DATE_CREATED\nDuration: ${DURATION:0:8}" \
    credits.png

# Convert image to video
ffmpeg -loop 1 -t 5 -i credits.png -vf "format=yuv420p" -c:v libx264 credits.mp4

# Convert AVI to MP4, preserving all audio streams
ffmpeg -i "$INPUT_AVI" -map 0 -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k output.mp4

# Concatenate credits with converted video
ffmpeg -i "credits.mp4" -i "output.mp4" -filter_complex \
"[0:v:0]scale=1280:720[credits]; [1:v:0]scale=1280:720[video]; [1:a:0][1:a:1]amerge=inputs=2[audio]; [credits][video][audio]concat=n=2:v=1:a=1[outv][outa]" \
-map "[outv]" -map "[outa]" final_output.mp4

echo "Conversion complete: final_output.mp4"
