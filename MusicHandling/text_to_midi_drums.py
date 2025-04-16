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
import sys
from patterns import get_pattern_with_snares

# === Constants ===
MIDI_NOTES = {'K': 36, 'S': 38}
STEP_DURATION = 0.25
TOTAL_STEPS = 32
DEFAULT_VELOCITY = 80

def parse_pattern(pattern_str):
    step_map = {}
    for token in pattern_str.split(','):
        if '-' not in token:
            continue
        step_str, instrs = token.strip().split('-')
        step = int(step_str.strip()) - 1
        entries = re.findall(r'([KS])(\d{1,3})?', instrs.strip().upper())
        note_data = []
        for symbol, vel_str in entries:
            pitch = MIDI_NOTES.get(symbol)
            velocity = int(vel_str) if vel_str else DEFAULT_VELOCITY
            note_data.append((pitch, velocity))
        step_map[step] = note_data
    return step_map

def build_score(step_map):
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
        else:
            p.insert(offset, note.Rest(quarterLength=STEP_DURATION))

    s = stream.Score()
    s.append(p)
    return s

def export_midi(score, output_file):
    mf = midi.translate.streamToMidiFile(score)
    for track in mf.tracks:
        for event in track.events:
            if event.type in ['NOTE_ON', 'NOTE_OFF']:
                event.channel = 9
    mf.open(output_file, 'wb')
    mf.write()
    mf.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py pattern_name")
        return

    pattern_id = sys.argv[1]
    try:
        pattern = get_pattern_with_snares(pattern_id)
    except ValueError as e:
        print(e)
        return

    step_map = parse_pattern(pattern)
    score = build_score(step_map)
    output_file = f"{pattern_id}.mid"
    export_midi(score, output_file)
    print(f"Exported '{output_file}' with snares + '{pattern_id}' pattern.")

if __name__ == "__main__":
    main()
