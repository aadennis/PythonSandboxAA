from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo
import random

# Constants
KICK = 36
SNARE = 38
CLOSED_HH = 42
OPEN_HH = 46
CRASH = 49

bpm = 123
ticks_per_beat = 480
swing_amount = 0.12  # Proportion of delay on swung 16th notes (0.0 to 0.5)

# Derived values
tempo = bpm2tempo(bpm)
sixteenth = ticks_per_beat // 4
swing_offset = int(sixteenth * swing_amount)

# Create the MIDI file
mid = MidiFile(ticks_per_beat=ticks_per_beat)
track = MidiTrack()
mid.tracks.append(track)

track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

def add_note(note, time, velocity=100, duration=0):
    track.append(Message('note_on', note=note, velocity=velocity, time=time))
    track.append(Message('note_off', note=note, velocity=0, time=duration))

def human_velocity(base, variation=10):
    return max(1, min(127, base + random.randint(-variation, variation)))

def add_bar(start_tick, hats='closed', add_crash=False):
    tick = start_tick
    for i in range(8):  # 8 eighth notes in a bar
        pos = i * 2  # convert to 16th-note position
        swing = swing_offset if i % 2 == 1 else 0

        # Hi-hat
        hh_note = CLOSED_HH if hats == 'closed' else OPEN_HH
        hh_velocity = human_velocity(70, 8)
        add_note(hh_note, tick, velocity=hh_velocity)
        tick = 0  # following notes will be relative to this

        # Kick pattern
        if pos in [0, 3, 4]:
            kick_velocity = human_velocity(100, 6)
            add_note(KICK, 0, velocity=kick_velocity)

        # Snare pattern (backbeat)
        if pos in [4, 12]:
            snr_velocity = human_velocity(110, 5)
            add_note(SNARE, 0, velocity=snr_velocity)

        # Apply swing to the following step
        tick = sixteenth * 2 + swing

    # Optional crash on beat 1
    if add_crash:
        add_note(CRASH, 0, velocity=120)

    return start_tick + ticks_per_beat * 4  # Advance by 1 bar

# Compose the beat
tick = 0

# 8-bar verse: closed hats
for _ in range(8):
    tick = add_bar(tick, hats='closed')

# 8-bar chorus: open hats, crash every 4 bars
for i in range(8):
    crash = i % 4 == 0
    tick = add_bar(tick, hats='open', add_crash=crash)

# Save the file
mid.save("sweet_caroline_humanized.mid")
print("Saved as sweet_caroline_humanized.mid")
