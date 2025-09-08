from mido import Message, MidiFile, MidiTrack, MetaMessage

# Create a new MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set time signature and tempo
track.append(MetaMessage('time_signature', numerator=4, denominator=4, time=0))
track.append(MetaMessage('set_tempo', tempo=500000))  # 120 BPM

# Define note mappings
note_map = {
    'A2': 45,
    'C3': 48,
    'E3': 52,
    'F2': 41
}

transpose = 12  # One octave
chord1 = [note_map['A2'] + transpose, note_map['C3'] + transpose, note_map['E3'] + transpose]
chord2 = [note_map['F2'] + transpose, note_map['A2'] + transpose, note_map['C3'] + transpose]


# Quarter note duration in ticks (default ticks_per_beat = 480)
quarter = 480
velocity = 64

# Add 4 bars of chord1
for _ in range(4):
    for note in chord1:
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
    for note in chord1:
        track.append(Message('note_off', note=note, velocity=velocity, time=quarter))

# Add 4 bars of chord2
for _ in range(4):
    for note in chord2:
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
    for note in chord2:
        track.append(Message('note_off', note=note, velocity=velocity, time=quarter))

# Save the file
mid.save('eight_bar_chords.mid')



