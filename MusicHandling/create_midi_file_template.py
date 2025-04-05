from mido import Message, MidiFile, MidiTrack, MetaMessage

# Create a new MIDI file
mid = MidiFile(ticks_per_beat=480)  # Standard PPQ setting
tempo = 60000000 // 95  # 95 BPM

# Function to create a MIDI track with 3/4 time signature and unique channel
def create_track(channel):
    track = MidiTrack()
    
    # Set instrument (Acoustic Grand Piano)
    track.append(Message('program_change', program=0, channel=channel))
    
    # Set time signature to 3/4
    track.append(MetaMessage('time_signature', numerator=3, denominator=4, time=0))
    
    for bar in range(1):
        # Note on (C4 = MIDI note 60)
        track.append(Message('note_on', note=60, velocity=64, time=0, channel=channel))
        # Note off (half note duration in 3/4 time)
        track.append(Message('note_off', note=60, velocity=64, time=480, channel=channel))  
    
    return track

# Create 3 tracks with different channels
for i in range(3):
    mid.tracks.append(create_track(i))  # Channels 0, 1, 2

# Save the MIDI file
mid.save("template_3-4.mid")
print("MIDI file saved as template_3-4.mid")
