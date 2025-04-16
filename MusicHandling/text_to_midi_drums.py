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

# === Your pattern ===
pattern = "1-K,3-SK,4-S,15-K,16-K,17-SK,31-K"

snares = "5-S,13-S,21-S,29-S,"
pattern01 = "1-K,5-S,9-K,13-S,17-K,21-S,25-K,29-S"
pattern02 = "1-K,5-S,9-K,13-S,17-K,21-S,25-K,27-K,29-S,30-K"
pattern03 = "1-K,5-S,9-K,11-K,13-S,17-K,21-S,23-K,27-K,29-S"
pattern04 = "1-K,3-K,7-K,11-K,15-K,19-K,23-K,25-K,27-K,28-K"
pattern05 = "1-K,3-K,7-K,9-K,12-K,15-K,18-K,20-K,23-K,25-K,27-K,31-K"
pattern06 = "1-K,9-K,15-K,17-K,19-K,20-K,23-K,25-K,27-K,31-K"
pattern07 = "1-K,3-K,4-K,7-K,9-K,12-K,15-K,19-K,20-K,23-K,24-K,26-K,28-K,31-K"
pattern08 = "1-K,3-K,9-K,11-K,17-K,19-K,23-K,27-K"

pattern = snares + pattern08

# example of dynamics support - ignore for now
#pattern = "1-K100,3-S,5-K70,9-K110,13-S,17-K,21-S,25-K85,29-S"

# === Constants ===
MIDI_NOTES = {'K': 36, 'S': 38}
STEP_DURATION = 0.25  # One 1/16th note
STEPS_PER_BAR = 16
TOTAL_STEPS = 32
DEFAULT_VELOCITY = 80

# === Parse your input ===
# Supports entries like: 1-K100, 5-S, 9-K70
step_map = {}  # step: list of (midi_pitch, velocity)
for token in pattern.split(','):
    if '-' not in token:
        continue
    step_str, instrs = token.strip().split('-')
    step = int(step_str.strip()) - 1  # 1-based to 0-based

    # Match instruments with optional velocity, e.g. K100 or just S
    entries = re.findall(r'([KS])(\d{1,3})?', instrs.strip().upper())
    note_data = []
    for symbol, vel_str in entries:
        pitch = MIDI_NOTES.get(symbol)
        velocity = int(vel_str) if vel_str else DEFAULT_VELOCITY
        note_data.append((pitch, velocity))
        step_map[step] = note_data

# === Create a single flat part ===
p = stream.Part()
p.append(tempo.MetronomeMark(number=100))
p.append(meter.TimeSignature('16/16'))

# Add all 32 steps as notes/rests
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
        r = note.Rest(quarterLength=STEP_DURATION)
        p.insert(offset, r)

# === Add to score and export MIDI ===
s = stream.Score()
s.append(p)

# Force MIDI channel 10
mf = midi.translate.streamToMidiFile(s)
for track in mf.tracks:
    for event in track.events:
        if event.type in ['NOTE_ON', 'NOTE_OFF']:
            event.channel = 9

mf.open('drum_fixed_corrected454.mid', 'wb')
mf.write()
mf.close()

print("Exported 'drum_fixed_corrected4.mid' with pattern-driven velocities.")
