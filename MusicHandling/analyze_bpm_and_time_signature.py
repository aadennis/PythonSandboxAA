'''
pip install numpy librosa soundfile matplotlib
The script takes an audio file as input and returns the estimated BPM 
using the Librosa library.    
Given that in many cases the time (4/5, 6/8, etc) is difficult to determine,
we will focus just on the BPM. Time signature would be nice, but the key
focus is to get the BPM right.

See below for findings, song by song. The assumed time signature is also 
included for reference, but it is not used in the BPM calculation.
'''
 
import librosa
import numpy as np

def analyze_bpm(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path, sr=None)

    # Compute onset envelope for better beat tracking
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    # Estimate tempo (BPM)
    tempo_array, _ = librosa.beat.beat_track(y=y, sr=sr, onset_envelope=onset_env)
    
    # Convert to float to avoid NumPy issues
    tempo = float(tempo_array) if isinstance(tempo_array, np.ndarray) else tempo_array

    return tempo

# Example usage

#file_path = "WildRover_ForBPM.mp3" # 120 BPM (6/8)
file_path = "WhiskeyInTheJar_ForBPM.mp3" # 105 BPM (4/4)

bpm = analyze_bpm(file_path)
print(f"Estimated BPM for [{file_path}]: [{round(bpm)}] BPM")
