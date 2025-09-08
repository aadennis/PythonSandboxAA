from mido import Message, MidiFile, MidiTrack, MetaMessage

# Create a new MIDI file and a track to hold MIDI events
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set the time signature (4/4) and tempo (120 BPM)
track.append(MetaMessage('time_signature', numerator=4, denominator=4, time=0))
track.append(MetaMessage('set_tempo', tempo=500000))  # Tempo in microseconds per beat

# Define note mappings for specific pitches
note_map = {
    'A2': 45,  # MIDI note number for A2
    'C3': 48,  # MIDI note number for C3
    'E3': 52,  # MIDI note number for E3
    'F2': 41   # MIDI note number for F2
}

# Transpose notes by one octave (12 semitones)
transpose = 12

# Define two chords using the transposed notes
chord1 = [note_map['A2'] + transpose, note_map['C3'] + transpose, note_map['E3'] + transpose]
chord2 = [note_map['F2'] + transpose, note_map['A2'] + transpose, note_map['C3'] + transpose]

# Define the duration of a quarter note in ticks (default ticks_per_beat = 480)
quarter = 480

# Define the velocity (volume) of the notes
velocity = 64

# Add 4 bars of chord1 to the track
for _ in range(4):  # Repeat for 4 bars
    for note in chord1:  # Turn on all notes in the chord
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
    for note in chord1:  # Turn off all notes in the chord after the quarter note duration
        track.append(Message('note_off', note=note, velocity=velocity, time=quarter))

# Add 4 bars of chord2 to the track
for _ in range(4):  # Repeat for 4 bars
    for note in chord2:  # Turn on all notes in the chord
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
    for note in chord2:  # Turn off all notes in the chord after the quarter note duration
        track.append(Message('note_off', note=note, velocity=velocity, time=quarter))

# Save the MIDI file with the specified name
mid.save('eight_bar_chords.mid')



