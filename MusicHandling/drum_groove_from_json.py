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
    ticks_per_step = config["ticks_per_beat"] // 4  # 16th note resolution

    last_step = 0
    for hit in config["pattern"]:
        step = hit["step"]
        note = config["instruments"][hit["instrument"]]
        
        # Calculate the delta time based on the step
        delta_time = (step - last_step) * ticks_per_step
        
        # Insert the 'note_on' message with the calculated delta time
        track.append(Message('note_on', note=note, velocity=100, time=delta_time, channel=channel))
        
        # Insert the 'note_off' message (with a short duration for the note)
        track.append(Message('note_off', note=note, velocity=0, time=ticks_per_step // 2, channel=channel))
        
        # Update the last step for the next iteration
        last_step = step

    mid.save(config["filename"])
    print(f"MIDI saved to: {config['filename']}")

# ---- Run it ----
if __name__ == "__main__":
    config = load_config("pattern_config.json")
    create_groove_from_config(config)


