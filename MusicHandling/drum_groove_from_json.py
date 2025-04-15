import json
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo

def load_config(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)

def create_groove_from_config(config: dict):
    mid = MidiFile(ticks_per_beat=config["ticks_per_beat"])
    track = MidiTrack()
    mid.tracks.append(track)

    # Tempo
    tempo = bpm2tempo(config["bpm"])
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

    # Channel 10 (zero-indexed = 9)
    channel = 9
    
    # Hard-coded trial for ticks_per_step
    ticks_per_step = 240  # (You can try different values here, like 120, 480, etc.)

    last_step = 0
    total_time = 0  # Debugging: To track the drift over multiple notes
    
    for hit in config["pattern"]:
        step = hit["step"]
        note = config["instruments"][hit["instrument"]]
        
        # Calculate delta_time based on hardcoded ticks_per_step
        delta_time = (step - last_step) * ticks_per_step
        total_time += delta_time
        
        # Insert the 'note_on' message with the calculated delta time
        track.append(Message('note_on', note=note, velocity=100, time=delta_time, channel=channel))
        
        # Insert the 'note_off' message (with a short duration for the note)
        track.append(Message('note_off', note=note, velocity=0, time=ticks_per_step // 2, channel=channel))
        
        # Update the last step for the next iteration
        last_step = step

    mid.save(config["filename"])
    print(f"MIDI saved to: {config['filename']}")
    print(f"Total time used (in ticks): {total_time}")  # Debugging line to track total time
    print(f"Drift over two measures: {total_time / config['ticks_per_beat']} beats")  # Track drift in terms of beats

# ---- Run it ----
if __name__ == "__main__":
    config = load_config("pattern_config.json")
    create_groove_from_config(config)

