# Lesson learned: do not use mido for creating MIDI files.
# A simple example of creating a one-bar MIDI file using music21
# pip install music21
# After hours of struggling with mido, I decided to try music21,
# and based on this simple example, it seems to be a much better choice.
# I was able to drag this into Ableton Live and it worked perfectly.
# This is the start of a simple drum track (Channel 10) 
# with a kick and snare (respectively MIDI note 36 (C1) and 38 (D1)).
from music21 import stream, note, tempo, meter, midi

# Create a new stream
s = stream.Stream()

# Set tempo to 100 BPM and time signature to 16/16
s.append(tempo.MetronomeMark(number=100))
s.append(meter.TimeSignature('16/16'))

# Create 16 1/16 notes: alternate Kick (36) and Snare (38)
drum_notes = [36 if i % 2 == 0 else 38 for i in range(16)]

for pitch in drum_notes:
    n = note.Note()
    n.pitch.midi = pitch
    n.quarterLength = 0.25  # 1/16 note = 0.25 quarter note
    n.storedInstrument = None  # Don't assign a melodic instrument
    s.append(n)

# Convert to MIDI and force channel 10 (index 9)
mf = midi.translate.streamToMidiFile(s)
for track in mf.tracks:
    for event in track.events:
        if event.type in ['NOTE_ON', 'NOTE_OFF']:
            event.channel = 9  # Channel 10

# Save to MIDI file
mf.open('drum_bar_16.mid', 'wb')
mf.write()
mf.close()

print("MIDI drum track exported as 'drum_bar_16.mid'")
