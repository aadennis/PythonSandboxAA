from mido import Message, MidiFile, MidiTrack, MetaMessage

# Create a new MIDI file
mid = MidiFile(ticks_per_beat=480)  # Standard PPQ setting
tempo = 60000000 // 95  # 95 BPM

# Add overarching song title in the first track (MuseScore uses this for the title)
title_track = MidiTrack()
title_track.append(MetaMessage('track_name', name="My MIDI Template", time=0))  # Song title
title_track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
title_track.append(MetaMessage('time_signature', numerator=3, denominator=4, time=0))
mid.tracks.append(title_track)

# Function to create a MIDI track with 3/4 time signature and unique channel
def create_track(channel, name):
    track = MidiTrack()
    
    # Track name (for MuseScore display)
    track.append(MetaMessage('track_name', name=name, time=0))
    
    # Set instrument (Acoustic Grand Piano)
    track.append(Message('program_change', program=0, channel=channel))
    
    for bar in range(1):
        # Note on (C4 = MIDI note 60)
        track.append(Message('note_on', note=60, velocity=64, time=0, channel=channel))
        # Note off (half note duration in 3/4 time)
        track.append(Message('note_off', note=60, velocity=64, time=480, channel=channel))  
    
    return track

# Create 3 tracks with different channels and unique names
mid.tracks.append(create_track(0, "Track 1"))
mid.tracks.append(create_track(1, "Track 2"))
mid.tracks.append(create_track(2, "Track 3"))

# Save the MIDI file
mid.save("output/template_with_song_title.mid")
print("MIDI file saved as template_with_song_title.mid")
