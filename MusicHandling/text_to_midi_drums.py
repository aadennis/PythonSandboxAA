# Lesson learned: do not use mido for creating MIDI files.
# A simple example of creating a one-bar MIDI file using music21
# pip install music21
# After hours of struggling with mido, I decided to try music21,
# and based on this simple example, it seems to be a much better choice.
# I was able to drag this into Ableton Live and it worked perfectly.
# This is a set of simple drum patterns (Channel 10) 
# with a kick and snare (respectively MIDI note 36 (C1) and 38 (D1)).
from music21 import stream, note, tempo, meter, midi, volume
import re
from patterns import snares, patterns

# === Constants ===
# === MIDI_NOTE Definitions ===
MIDI_NOTES = {
    'K': (36, 80),   # Kick
    'S': (38, 80),   # Snare
    'P': (44, 80),   # Pedal Hi-Hat
    'C': (42, 80),   # Closed Hi-Hat
    'Q': (46, 60),   # Quarter-Open Hi-Hat (lower velocity)
    'O': (46, 100),  # Open Hi-Hat (higher velocity)
}
STEP_DURATION = 0.25
STEPS_PER_BAR = 16
TOTAL_STEPS = 32
DEFAULT_VELOCITY = 80

def parse_pattern(pattern_string):
    step_map = {}  # step: list of (midi_pitch, velocity)
    for token in pattern_string.split(','):
        if '-' not in token:
            continue
        step_str, instrs = token.strip().split('-')
        step = int(step_str.strip()) - 1  # 1-based to 0-based

        # Match instruments with optional velocity, e.g. K100 or just S
        entries = re.findall(r'([KSQCO])(\d{1,3})?', instrs.strip().upper())
        note_data = []
        for symbol, vel_str in entries:
            pitch, default_vel = MIDI_NOTES.get(symbol, (None, DEFAULT_VELOCITY))
            if pitch is None:
                continue  # Skip if we get an unknown symbol
            velocity = int(vel_str) if vel_str else default_vel
            note_data.append((pitch, velocity))

        if step in step_map:
            step_map[step].extend(note_data)  # Append to existing notes at this step
        else:
            step_map[step] = note_data  # First time seeing this step

        # Debug: Print the step map after parsing
        print(f"Step Map: {step_map}")
    return step_map


def build_stream(step_map):
    p = stream.Part()
    p.append(tempo.MetronomeMark(number=100))
    p.append(meter.TimeSignature('16/16'))

    for i in range(TOTAL_STEPS):
        offset = i * STEP_DURATION
        if i in step_map:
            for pitch, velocity in step_map[i]:
                n = note.Note()
                n.pitch.midi = pitch
                n.quarterLength = STEP_DURATION
                n.offset = offset
                n.storedInstrument = None
                v = volume.Volume()
                v.velocity = velocity
                n.volume = v
                p.insert(offset, n)
                 # Debug: Print each note being added
                print(f"Adding Note: Pitch {pitch} Velocity {velocity} at offset {offset}")
        
        else:
            r = note.Rest(quarterLength=STEP_DURATION)
            p.insert(offset, r)

    return p

def save_midi(score_stream, filename):
    mf = midi.translate.streamToMidiFile(score_stream)
    for track in mf.tracks:
        for event in track.events:
            if event.type in ['NOTE_ON', 'NOTE_OFF']:
                event.channel = 9  # Channel 10 is 9 in 0-indexed
    mf.open(filename, 'wb')
    mf.write()
    mf.close()

def main(pattern_name):
    if pattern_name not in patterns:
        print(f"Pattern '{pattern_name}' not found.")
        return

    pattern = snares + patterns[pattern_name]
    print(f"Generating pattern: {pattern_name} with pattern: {pattern}")  # Debug
   
    step_map = parse_pattern(pattern)
    part = build_stream(step_map)

    s = stream.Score()
    s.append(part)

    filename = f"{pattern_name}.mid"
    save_midi(s, filename)
    print(f"Exported '{filename}' with pattern: {pattern}")

if __name__ == "__main__":
    # Run via terminal or IDE with main('pattern01') for example
    main("pattern14b")
