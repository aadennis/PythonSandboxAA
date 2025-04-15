from mido import Message, MidiFile, MidiTrack, bpm2tempo

def create_simple_backbeat(filename="sweet_caroline_style2.mid"):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Set tempo and time signature
    bpm = 123
    tempo = bpm2tempo(bpm)
    track.append(Message('program_change', program=0, time=0))  # Use default kit

    # MIDI constants
    kick = 36   # C1
    snare = 38  # D1
    ticks_per_beat = mid.ticks_per_beat
    sixteenth = ticks_per_beat // 4

    # Two bars of 4/4, 16th note resolution
    pattern = [
        (0,  kick),   # 1
        (4,  snare),  # 1e&a = +4
        (8,  kick),   # 2
        (12, snare),  # 2e&a = +4
        (16, kick),   # 3
        (20, snare),  # 3e&a = +4
        (24, kick),   # 4
        (28, snare),  # 4e&a = +4
    ]

    # Duplicate pattern for both measures
    for measure in range(2):
        for step, note in pattern:
            abs_tick = measure * 16 + step
            delta_time = (step - pattern[pattern.index((step, note))-1][0]) if step != 0 else 0
            track.append(Message('note_on', note=note, velocity=100, time=sixteenth * delta_time))
            track.append(Message('note_off', note=note, velocity=100, time=sixteenth))

    filename=f"output/{filename}"
    mid.save(filename)
    print(f"MIDI saved to {filename}")

create_simple_backbeat()

