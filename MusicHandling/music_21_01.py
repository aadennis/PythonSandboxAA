# Lesson learned: do not use mido for creating MIDI files.
# A simple example of creating a one-bar MIDI file using music21
# pip install music21
# After hours of struggling with mido, I decided to try music21,
# and based on this simple example, it seems to be a much better choice.
# I was able to drag this into Ableton Live and it worked perfectly.
# This is the start of a simple drum track with a kick and snare.
# Right now, it lacks the channel 10 instruction required by midi for
# drums, but is evidently being interpreted as channel 10 by Ableton Live.
# Also AL must be assuming C3, whatever drum instrument that is.
# But it's a start.
from music21 import stream, note, tempo, meter

s = stream.Stream()
s.append(tempo.MetronomeMark(number=100))
s.append(meter.TimeSignature('4/4'))

# Add four 1/8 notes and four 1/8 rests (alternating).
# This with a note on the first 1/8, and ends with a rest.
for _ in range(4):
    s.append(note.Note(type='eighth'))
    s.append(note.Rest(type='eighth'))

# Export to MIDI
s.write('midi', fp='one_bar.mid')
print("MIDI file exported as 'one_bar.mid'")
