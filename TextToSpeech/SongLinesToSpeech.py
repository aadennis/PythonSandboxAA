import pyttsx3
import re
from pydub import AudioSegment
import time

# Configuration
input_file = 'test_song_01.txt'  # Input text file
output_file = 'output.wav'  # Output file
speech_delay = 2  # Delay before speech in seconds
temp_file = 'temp_song.txt'  # Temporary file to store "go" prepended text

# Load song text
with open(input_file, 'r') as file:
    song_text = file.read()

# Remove text in brackets and split into lines
song_lines = re.sub(r'\[.*?\]', '', song_text).splitlines()

# Prepend "go" to each line and save to the temporary text file
with open(temp_file, 'w') as temp_f:
    for line in song_lines:
        line = line.strip()
        if line:  # Skip empty lines
            temp_f.write(f"go {line}\n")

print(f"Temporary file {temp_file} created with 'go' prepended.")

# Step 2: Initialize pyttsx3 engine and process the temporary text file
engine = pyttsx3.init()

# Create a list of audio segments
audio_segments = []

# Read the modified text (with "go") from the temp file
with open(temp_file, 'r') as temp_f:
    for line in temp_f:
        line = line.strip()
        if line:  # Skip empty lines
            # Convert the line (with "go") to speech
            engine.save_to_file(line, 'temp.wav')
            engine.runAndWait()

            # Load the speech audio
            speech = AudioSegment.from_wav('temp.wav')

            # Add speech to the audio segments list
            audio_segments.append(speech)

            # Wait for the speech delay before the next line
            time.sleep(speech_delay)

# Combine all the audio segments
final_audio = AudioSegment.empty()
for segment in audio_segments:
    final_audio += segment

# Export the final audio to WAV
final_audio.export(output_file, format='wav')
print(f"Audio saved to {output_file}")
