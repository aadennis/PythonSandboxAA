# This script consolidates song metadata from individual JSON files in the "Instructions" folder
# into a single JSON file named "song_metadata.json".
import json
import os
import json

input_folder = "Instructions"
output_file = os.path.join(input_folder, "song_metadata.json")

all_metadata = []

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        title = os.path.splitext(filename)[0]
        with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
            data = json.load(f)
            data["title"] = title
            all_metadata.append(data)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_metadata, f, indent=2)

