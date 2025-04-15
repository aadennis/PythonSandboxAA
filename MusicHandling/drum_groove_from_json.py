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
    
    # Hardcoded trial for ticks_per_step
    ticks_per_step = config["ticks_per_beat"] // 4  # 16th note resolution
    
    last_step = 0
    total_time = 0  # Debugging: To track the drift over multiple notes
    expected_ticks_for_2_measures = 1920 * 2  # 2 measures = 3840 ticks

    # Adjust pattern to fill exactly two measures (3840 ticks)
    num_steps = len(config["pattern"])  # Number of steps in the pattern
    step_interval = expected_ticks_for_2_measures // num_steps  # Evenly space steps

    for hit in config["pattern"]:
        step = hit["step"]
        note = config["instruments"][hit["instrument"]]
        
        # Adjust delta_time to space the steps evenly across 2 measures
        delta_time = step_interval
        total_time += delta_time
        
        # Insert the 'note_on' message with the calculated delta time
        track.append(Message('note_on', note=note, velocity=100, time=delta_time, channel=channel))
        
        # Insert the 'note_off' message right after the 'note_on' (same step length for note off)
        track.append(Message('note_off', note=note, velocity=0, time=step_interval, channel=channel))

    mid.save(config["filename"])
    print(f"MIDI saved to: {config['filename']}")
    print(f"Total time used (in ticks): {total_time}")  # Debugging line to track total time
    print(f"Drift over two measures: {total_time / config['ticks_per_beat']} beats")  # Track drift in terms of beats

    # Debug: Verify if the pattern is within 2 measures
    if total_time > expected_ticks_for_2_measures:
        print("Warning: Pattern duration exceeds 2 measures!")

# ---- Run it ----
if __name__ == "__main__":
    config = load_config("pattern_config.json")
    create_groove_from_config(config)
