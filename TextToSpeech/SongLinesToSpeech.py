import pyttsx3
import re
from pydub import AudioSegment
import os
import sys

def lyrics_to_speech(input_file, speech_rate=160, speech_delay=10):
    """
    Convert a text file of lyrics into a spoken WAV file, with pauses between lines.
    The output is saved as a WAV file with the same name as the input file, but with 
    the extension ".out.wav".
    Ignore any text within square brackets (e.g., [Chorus]), and the brackets themselves, as 
    my convention for song lyrics is to put the chords in square brackets - we don't want to
    hear those chord names.

    Args:
        input_file (str): Path to the text file.
        speech_rate (int): Words per minute (default: 160).
        speech_delay (int): Pause duration between lines in seconds (default: 10).
    """
    output_file = os.path.splitext(input_file)[0] + '.out.wav'
    pause_duration = speech_delay * 1000  # Convert delay to milliseconds

    # Load song text
    with open(input_file, 'r') as file:
        song_text = file.read()

    # Remove text in brackets and split into lines
    song_lines = [line.strip() for line in re.sub(r'\[.*?\]', '', song_text).splitlines() if line.strip()]

    # Initialize pyttsx3 engine
    engine = pyttsx3.init()
    engine.setProperty('rate', speech_rate)  # Adjust speech speed

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


def main():
    # Get input file from command-line argument or use default
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'ManchesterRambler.txt'
    
    # Run the text-to-speech conversion
    lyrics_to_speech(input_file)


if __name__ == "__main__":
    main()
