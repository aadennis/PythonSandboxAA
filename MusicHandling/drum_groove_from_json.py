import json
from mido import Message, MidiFile, MidiTrack, bpm2tempo

def load_groove_config(path):
    with open(path, 'r') as f:
        return json.load(f)

def create_groove_from_config(config_path):
    cfg = load_groove_config(config_path)

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    bpm = cfg["bpm"]
    tempo = bpm2tempo(bpm)
    mid.ticks_per_beat = 480  # default; can be changed if needed
    sixteenth = mid.ticks_per_beat // cfg["steps_per_beat"]

    total_steps = cfg["beats_per_bar"] * cfg["steps_per_beat"] * cfg["bars"]

    # Flatten events into list of (step_index, midi_note)
    events = []
    for drum_name, steps in cfg["pattern"].items():
        midi_note = cfg["kit"].get(drum_name)
        if midi_note is not None:
            for step in steps:
                if 0 <= step < total_steps:
                    events.append((step, midi_note))

    # Sort events by step
    events.sort()

    # Track delta time between steps
    last_step = 0
    for step, note in events:
        delta = step - last_step
        track.append(Message('note_on', note=note, velocity=100, time=sixteenth * delta))
        track.append(Message('note_off', note=note, velocity=100, time=sixteenth))
        last_step = step

    mid.save(cfg["filename"])
    print(f"MIDI saved to {cfg['filename']}")

# Example usage
create_groove_from_config("groove_config.json")
