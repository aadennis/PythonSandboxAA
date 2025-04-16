# Lesson learned: do not use mido for creating MIDI files.
# A simple example of creating a one-bar MIDI file using music21
# pip install music21
# After hours of struggling with mido, I decided to try music21,
# and based on this simple example, it seems to be a much better choice.
# I was able to drag this into Ableton Live and it worked perfectly.
# This is the start of a simple drum track (Channel 10) 
# with a kick and snare (respectively MIDI note 36 (C1) and 38 (D1)).
from music21 import stream, note, tempo, meter, midi

# ===== Config =====
pattern = "1-K,3-SK,4-S,32-K"  # Your drum pattern input

# MIDI note mapping
MIDI_NOTES = {'K': 36, 'S': 38}  # Kick and Snare

# Parse pattern into a dict: step_num -> list of MIDI notes
step_map = {}
for token in pattern.split(','):
    if '-' not in token:
        continue
    step_str, instrs = token.split('-')
    step = int(step_str.strip()) - 1  # 0-based index
    midi_notes = [MIDI_NOTES[c] for c in instrs.strip() if c in MIDI_NOTES]
    step_map[step] = midi_notes

# Create stream
s = stream.Stream()
s.append(tempo.MetronomeMark(number=100))
s.append(meter.TimeSignature('16/16'))

# Build 32 steps (2 bars of 16/16)
for i in range(32):
    if i in step_map:
        for pitch in step_map[i]:
            n = note.Note()
            n.pitch.midi = pitch
            n.quarterLength = 0.25  # 1/16 note
            n.storedInstrument = None
            s.append(n)
    else:
        s.append(note.Rest(quarterLength=0.25))

# Convert to MIDI and force channel 10 (index 9)
mf = midi.translate.streamToMidiFile(s)
for track in mf.tracks:
    for event in track.events:
        if event.type in ['NOTE_ON', 'NOTE_OFF']:
            event.channel = 9

mf.open('drum_pattern3.mid', 'wb')
mf.write()
mf.close()

print("Drum MIDI exported as 'drum_pattern3.mid'")
