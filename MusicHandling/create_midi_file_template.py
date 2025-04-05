from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile(ticks_per_beat=480)  # Standard PPQ setting
tempo = 60000000 // 95  # 95 BPM

# Function to create a MIDI track with C4 half-notes
def create_track():
    track = MidiTrack()
    for bar in range(12):
        # Note on (C4 = MIDI note 60)
        track.append(Message('note_on', note=60, velocity=64, time=0))
        # Note off (after half-note duration)
        track.append(Message('note_off', note=60, velocity=64, time=480))  # Half note at 95 BPM
    return track

# Create 3 tracks
for _ in range(3):
    mid.tracks.append(create_track())

# Save the MIDI file
mid.save("template.mid")
print("MIDI file saved as template.mid")


