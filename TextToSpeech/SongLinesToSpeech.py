import pyttsx3
import re
from pydub import AudioSegment
import time

# Configuration
input_file = 'wild.txt'  # Input text file
output_file = 'output.wav'  # Output file
speech_delay = 2  # Delay before speech in seconds
go_pause_duration = 1  # Duration of pause after the word "go" (in seconds)

# Load song text
with open(input_file, 'r') as file:
    song_text = file.read()

# Remove text in brackets and split into lines
song_lines = re.sub(r'\[.*?\]', '', song_text).splitlines()

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Create a list of audio segments
audio_segments = []

for line in song_lines:
    line = line.strip()
    if line:  # Skip empty lines
        # Prepend "go" and insert a pause after it
        modified_line = f"go {line}"

        # Convert the modified line (with "go") to speech
        engine.save_to_file(modified_line, 'temp.wav')
        engine.runAndWait()

        # Load the speech audio
        speech = AudioSegment.from_wav('temp.wav')

        # Add speech to the audio segments list
        audio_segments.append(speech)

        # Add a pause after the "go" part (to simulate a delay)
        pause = AudioSegment.silent(duration=go_pause_duration * 1000)  # Duration in milliseconds
        audio_segments.append(pause)

        # Wait for the speech delay before the next line
        time.sleep(speech_delay)

# Combine all the audio segments
final_audio = AudioSegment.empty()
for segment in audio_segments:
    final_audio += segment

# Export the final audio to WAV
final_audio.export(output_file, format='wav')
print(f"Audio saved to {output_file}")
