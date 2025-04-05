from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile(ticks_per_beat=480)  # Standard PPQ setting
tempo = 60000000 // 95  # 95 BPM

# Function to create a MIDI track with a unique channel
def create_track(channel):
    track = MidiTrack()
    track.append(Message('program_change', program=0, channel=channel))  # Assign an instrument (Acoustic Grand Piano)
    for bar in range(1):
        track.append(Message('note_on', note=60, velocity=64, time=0, channel=channel))
        track.append(Message('note_off', note=60, velocity=64, time=480, channel=channel))  # Half note
    return track

# Create 3 tracks with different channels
for i in range(3):
    mid.tracks.append(create_track(i))  # Channels 0, 1, 2

# Save the MIDI file
mid.save("template_fixed.mid")
print("MIDI file saved as template_fixed.mid")
