import pyttsx3
import re
from pydub import AudioSegment
import os

# Configuration
input_file = 'wild.txt'  # Input text file
# Generate output file name by appending ".out.wav" to the input file name (without extension)
output_file = os.path.splitext(input_file)[0] + '.out.wav'
speech_delay = 2  # Delay between speech lines (in seconds)
temp_file = 'temp_song.txt'  # Temporary file to store "go" on its own line
pause_duration = speech_delay * 1000  # Convert speech delay to milliseconds

# Load song text
with open(input_file, 'r') as file:
    song_text = file.read()

# Remove text in brackets and split into lines
song_lines = re.sub(r'\[.*?\]', '', song_text).splitlines()

# Prepend "go" on its own line before each actual song line
with open(temp_file, 'w') as temp_f:
    for line in song_lines:
        line = line.strip()
        if line:  # Skip empty lines
            temp_f.write("go!\n")  # Add "go" before each line
            temp_f.write(f"{line}\n")  # Write the song line after "go"

print(f"Temporary file {temp_file} created with 'go' on its own line.")

# Step 2: Initialize pyttsx3 engine and process the temporary text file
engine = pyttsx3.init()

# Create a list of audio segments
audio_segments = []

# Read the modified text (with "go" on its own line) from the temp file
with open(temp_file, 'r') as temp_f:
    for line in temp_f:
        line = line.strip()
        if line:  # Skip empty lines
            if line == "go!":
                # Convert "go" with no pause before it
                engine.save_to_file(line, 'temp.wav')
                engine.runAndWait()

                # Load the speech audio
                speech = AudioSegment.from_wav('temp.wav')

                # Add speech to the audio segments list
                audio_segments.append(speech)

                # Insert a silent pause only after "go"
                silence = AudioSegment.silent(duration=pause_duration)
                audio_segments.append(silence)
            else:
                # Convert the song line
                engine.save_to_file(line, 'temp.wav')
                engine.runAndWait()

                # Load the speech audio
                speech = AudioSegment.from_wav('temp.wav')

                # Add speech to the audio segments list
                audio_segments.append(speech)

# Combine all the audio segments
final_audio = AudioSegment.empty()
for segment in audio_segments:
    final_audio += segment

# Export the final audio to WAV with the dynamic output file name
final_audio.export(output_file, format='wav')
print(f"Audio saved to {output_file}")
