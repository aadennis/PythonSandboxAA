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



def extrapolate_chords(c_root_data: List[Dict[str, str]]) -> Generator[Dict[str, str], None, None]:
    chromatic_roots = ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    for root in chromatic_roots:
        root_midi = NOTE_TO_MIDI[root]
        for entry in c_root_data:
            base_root = note_to_midi(entry['root'])
            interval_offsets = [
                note_to_midi(entry[k]) - base_root
                for k in ['key2', 'key3', 'key4', 'key5']
                if entry.get(k)
            ]
            new_root_midi = root_midi + (base_root // 12) * 12
            if new_root_midi < base_root:
                new_root_midi += 12  # Extend upward if needed

            new_entry = {
                'chord_id': entry['chord_id'].replace('c_', f"{root.lower()}_"),
                'name': entry['name'].replace('C', root),
                'comments': entry.get('comments', ''),
                'tested': '',
                'root': midi_to_note(new_root_midi)
            }

            for i, offset in enumerate(interval_offsets):
                new_entry[f'key{i+2}'] = midi_to_note(new_root_midi + offset)

            yield new_entry

# Sample input (C-root chords)
c_root_data = [
    {'chord_id': 'c_maj', 'name': 'C Major', 'root': 'C3', 'key2': 'E3'},
    {'chord_id': 'c_maj7', 'name': 'C Major 7', 'root': 'C3', 'key2': 'E3', 'key3': 'B2'},
    # Add more entries as needed...
]

for chord in extrapolate_chords(c_root_data):
    print(chord)            