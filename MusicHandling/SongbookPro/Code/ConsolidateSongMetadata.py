# This script consolidates song metadata from individual JSON files in the "Metadata" folder
# into a single JSON file named "song_metadata.json".
import json
import os
import datetime
import re
import shutil
import pandas as pd

def consolidate_metadata():
    """
    Consolidates song metadata from individual JSON files in the "Metadata" folder
    into a single JSON file named "song_metadata.json".
    Undecided if this function will be used again
    """
    input_folder = "Metadata"
    metadata_file_all_songs = os.path.join(input_folder, "song_metadata.json")

    #Backup existing song_metadata.json with timestamp
    if os.path.exists(metadata_file_all_songs):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file = os.path.join(
            input_folder, f"song_metadata[{timestamp}].json"
        )
        shutil.copy2(metadata_file_all_songs, backup_file)

    with open(metadata_file_all_songs, "r", encoding="utf-8") as f:
        try:
            existing_metadata = json.load(f)
        except json.JSONDecodeError:
            existing_metadata = []


    all_metadata = existing_metadata.copy()

    for filename in os.listdir(input_folder):
        if filename.endswith(".json") and not re.match(r"song_metadata.*\.json$", filename):
            # Must have the metadata for an individual song
            title = os.path.splitext(filename)[0]
            with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                data["title"] = title
                all_metadata.append(data)

    with open(metadata_file_all_songs, "w", encoding="utf-8") as f:
        json.dump(all_metadata, f, indent=2)

def add_json_attribute(in_file: str):
    df = pd.read_json(in_file)
    print(df.head(10))

def set_default_value(in_file: str):
    """
    Given a hard-coded (TODO) json attribute, set all records to 
    a default value.
    BTW, test data shows that [/] is intentionally escaped to [\/] by pd
    """
    df = pd.read_json(in_file)
    print(df.head(10))
    df['scroll_speed'] = 2.7
    print(df.head(10))
    df.to_json(in_file, orient='records', indent=4, )
    

if __name__ == '__main__':
    songs_file = 'Metadata/song_metadata.json'
    set_default_value(songs_file)

