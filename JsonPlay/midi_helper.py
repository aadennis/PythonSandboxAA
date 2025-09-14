from typing import List, Dict, Generator
import re

# MIDI note mapping
NOTE_TO_MIDI = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8,
    'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
}
MIDI_TO_NOTE = {v: k for k, v in NOTE_TO_MIDI.items() if '#' not in k}  # Normalize to flats

def note_to_midi(note: str) -> int:
    match = re.match(r'^([A-G][b#]?)(\d)$', note)
    if not match:
        raise ValueError(f"Invalid note format: {note}")
    pitch, octave = match.groups()
    return NOTE_TO_MIDI[pitch] + int(octave) * 12

def midi_to_note(midi: int) -> str:
    pitch = MIDI_TO_NOTE[midi % 12]
    octave = midi // 12
    return f"{pitch}{octave}"

