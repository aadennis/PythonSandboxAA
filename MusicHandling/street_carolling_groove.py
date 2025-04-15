from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo

def create_sweet_caroline_groove(filename='sweet_caroline_groove.mid'):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Settings
    bpm = 123
    ppq = mid.ticks_per_beat  # usually 480
    bar_ticks = ppq * 4
    eighth_note = ppq // 2
    quarter_note = ppq

    # Drum notes (General MIDI)
    kick = 36    # C1
    snare = 38   # D1
    hihat = 42   # F#1 closed

    # Meta messages
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm), time=0))
    track.append(MetaMessage('time_signature', numerator=4, denominator=4, time=0))

    # List to hold all events with absolute timing
    events = []

    for bar in range(8):
        bar_start = bar * bar_ticks

        # Hi-hats on 8th notes (1 & 2 & 3 & 4 &)
        for i in range(8):
            tick = bar_start + i * eighth_note
            events.append((tick, Message('note_on', note=hihat, velocity=60, time=0)))
            events.append((tick + ppq // 8, Message('note_off', note=hihat, velocity=0, time=0)))

        # Kick on 1 and 3
        for i in [0, 2]:
            tick = bar_start + i * quarter_note
            events.append((tick, Message('note_on', note=kick, velocity=100, time=0)))
            events.append((tick + ppq // 4, Message('note_off', note=kick, velocity=0, time=0)))

        # Snare on 2 and 4
        for i in [1, 3]:
            tick = bar_start + i * quarter_note
            events.append((tick, Message('note_on', note=snare, velocity=100, time=0)))
            events.append((tick + ppq // 4, Message('note_off', note=snare, velocity=0, time=0)))

    # Sort by absolute tick time
    events.sort(key=lambda x: x[0])

    # Convert absolute ticks to delta times
    last_tick = 0
    for tick, msg in events:
        delta = tick - last_tick
        msg.time = delta
        track.append(msg)
        last_tick = tick

    # Save MIDI file
    mid.save(filename)
    print(f"✅ MIDI saved as: {filename}")

if __name__ == '__main__':
    create_sweet_caroline_groove()
