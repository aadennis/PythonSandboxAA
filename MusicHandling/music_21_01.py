# Lesson learned: do not use mido for creating MIDI files.
# A simple example of creating a one-bar MIDI file using music21
# pip install music21
# After hours of struggling with mido, I decided to try music21,
# and based on this simple example, it seems to be a much better choice.
# I was able to drag this into Ableton Live and it worked perfectly.
# This is the start of a simple drum track (Channel 10) 
# with a kick and snare (respectively MIDI note 36 (C1) and 38 (D1)).
from music21 import stream, note, tempo, meter, midi

# Create a stream
s = stream.Stream()

# Set tempo and time signature
s.append(tempo.MetronomeMark(number=100))
s.append(meter.TimeSignature('4/4'))

# Alternate between kick (36) and snare (38)
drum_notes = [36, 38, 36, 38, 36, 38, 36, 38]

for pitch in drum_notes:
    n = note.Note()
    n.pitch.midi = pitch
    n.quarterLength = 0.5  # 1/8 note
    n.storedInstrument = None  # Make sure it doesn’t default to Piano
    s.append(n)
    s.append(note.Rest(quarterLength=0.5))  # 1/8 rest

# Write to MIDI using a custom MIDIFile to force channel 10
mf = midi.translate.streamToMidiFile(s)
for track in mf.tracks:
    for event in track.events:
        if event.isDeltaTime() or event.type != 'NOTE_ON':
            continue
        event.channel = 9  # Channel 10 in MIDI is index 9

mf.open('drum_bar2.mid', 'wb')
mf.write()
mf.close()

print("Drum MIDI file exported as 'drum_bar.mid'")
