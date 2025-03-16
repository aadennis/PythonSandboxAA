# Given a text file being the words of a song, render as speech.
# With these requirements:
# 1. Each line of the song should be spoken as a separate audio segment.
# 2. A pause of 5 seconds should be inserted between each line of the song.
# 3. The output should be saved as a WAV file with the same name as the input file, but with the extension ".out.wav".
# 4. Ignore any text within square brackets (e.g., [Chorus]), and the brackets themselves.

import pyttsx3
import re
from pydub import AudioSegment
import os

# Configuration
speech_rate = 160  # Speech rate (words per minute)
input_file = 'ManchesterRambler.txt'  # Input text file
output_file = os.path.splitext(input_file)[0] + '.out.wav'  # Output WAV file
speech_delay = 10  # Delay between speech lines (in seconds)
pause_duration = speech_delay * 1000  # Convert speech delay to milliseconds

# Load song text
with open(input_file, 'r') as file:
    song_text = file.read()

# Remove text in brackets and split into lines
song_lines = [line.strip() for line in re.sub(r'\[.*?\]', '', song_text).splitlines() if line.strip()]

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', speech_rate)  # Adjust speed (default is around 200)

# Create a list of audio segments
audio_segments = []

for line in song_lines:
    engine.save_to_file(line, 'temp.wav')
    engine.runAndWait()

    # Load the speech audio
    speech = AudioSegment.from_wav('temp.wav')

    # Add speech to the audio segments list
    audio_segments.append(speech)

    # Insert a silent pause after each spoken line
    silence = AudioSegment.silent(duration=pause_duration)
    audio_segments.append(silence)

# Combine all the audio segments
final_audio = sum(audio_segments, AudioSegment.empty())

# Export the final audio to WAV
final_audio.export(output_file, format='wav')
print(f"Audio saved to {output_file}")
