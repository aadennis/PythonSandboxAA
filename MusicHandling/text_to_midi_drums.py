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

# === Your pattern ===
pattern = "1-Kf,2-K,3-Kp,4-K,5-S90,6-S,7-Smp,8-Kff"

# === Constants ===
MIDI_NOTES = {'K': 36, 'S': 38}
DYNAMICS = {'pp': 40, 'p': 55, 'mp': 70, 'mf': 85, 'f': 100, 'ff': 115}
DEFAULT_DYNAMIC = 'mf'
DEFAULT_VELOCITY = DYNAMICS[DEFAULT_DYNAMIC]

STEP_DURATION = 0.25
TOTAL_STEPS = 32

# === Parse pattern with velocity logic ===
step_map = {}  # step: list of (midi_pitch, velocity)

for token in pattern.split(','):
    if '-' not in token:
        continue
    step_str, instrs = token.strip().split('-')
    step = int(step_str.strip()) - 1  # Convert to 0-based

    # Match things like Kf, Sff, K120, Sp, etc.
    entries = re.findall(r'([KS])((?:pp|mp|mf|ff|p|f)|\d{1,3})?', instrs.strip().lower())

    note_data = []
    for symbol, dyn in entries:
        pitch = MIDI_NOTES[symbol.upper()]
        if dyn in DYNAMICS:
            velocity = DYNAMICS[dyn]
        elif dyn.isdigit():
            velocity = int(dyn)
        else:
            velocity = DEFAULT_VELOCITY  # fallback
        note_data.append((pitch, velocity))
    step_map[step] = note_data

# === Create part ===
p = stream.Part()
p.append(tempo.MetronomeMark(number=100))
p.append(meter.TimeSignature('16/16'))

# Add all steps as notes or rests
for i in range(TOTAL_STEPS):
    offset = i * STEP_DURATION
    if i in step_map:
        for pitch, velocity in step_map[i]:
            n = note.Note()
            n.pitch.midi = pitch
            n.quarterLength = STEP_DURATION
            n.offset = offset
            n.storedInstrument = None
            n.volume = volume.Volume(velocity=velocity)
            p.insert(offset, n)
    else:
        p.insert(offset, note.Rest(quarterLength=STEP_DURATION))

# === Build MIDI score ===
s = stream.Score()
s.append(p)

# Force channel 10 for drums
mf = midi.translate.streamToMidiFile(s)
for track in mf.tracks:
    for event in track.events:
        if event.type in ['NOTE_ON', 'NOTE_OFF']:
            event.channel = 9

mf.open('drum_dynamics_demo.mid', 'wb')
mf.write()
mf.close()

print("✅ Exported 'drum_dynamics_demo.mid' with musical dynamics and velocity support.")
