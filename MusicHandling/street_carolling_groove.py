from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo

# General MIDI drum note numbers
KICK = 36
SNARE = 38
CLOSED_HH = 42
OPEN_HH = 46
CRASH = 49

# Tempo and timing
bpm = 123
tempo = bpm2tempo(bpm)
ticks_per_beat = 480  # Standard resolution
sixteenth = ticks_per_beat // 4

# Create MIDI file and track
mid = MidiFile(ticks_per_beat=ticks_per_beat)
track = MidiTrack()
mid.tracks.append(track)

# Set the tempo
track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

# Function to add a note to the track
def add_note(track, note, time, velocity=100, duration=0):
    track.append(Message('note_on', note=note, velocity=velocity, time=time))
    track.append(Message('note_off', note=note, velocity=0, time=duration))

# Function to build a 1-bar groove
def add_bar(kick_on=[0, 6], snare_on=[4, 12], hh_note=CLOSED_HH):
    for i in range(16):  # 16 sixteenth notes per bar
        time = sixteenth if i > 0 else 0
        step_time = time

        if i in kick_on:
            add_note(track, KICK, time=step_time, duration=0)
            step_time = 0
        if i in snare_on:
            add_note(track, SNARE, time=step_time, duration=0)
            step_time = 0
        if i % 2 == 0:  # Eighth note hats
            add_note(track, hh_note, time=step_time, velocity=70, duration=0)
        else:
            # If nothing is happening at this step, we still need to move time forward
            track.append(Message('note_off', note=0, velocity=0, time=step_time))

# Verse: 8 bars with closed hats
for _ in range(8):
    add_bar()

# Chorus: 8 bars with open hats + crash every 4 bars
for i in range(8):
    if i % 4 == 0:
        add_note(track, CRASH, time=0, velocity=110, duration=0)
    add_bar(hh_note=OPEN_HH)

# Save the file
mid.save("output/street_carolling_groove.mid")
print("MIDI file saved as 'street_carolling_groove.mid'")
