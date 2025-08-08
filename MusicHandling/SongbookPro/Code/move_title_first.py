import json

# filepath: d:\Sandbox\git\aadennis\PythonSandboxAA\MusicHandling\SongbookPro\Instructions\song_metadata.json
with open("d:/Sandbox/git/aadennis/PythonSandboxAA/MusicHandling/SongbookPro/Instructions/song_metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def move_title_first(song):
    if "title" in song:
        # Create a new dict with "title" first, then the rest
        return {"title": song["title"], **{k: v for k, v in song.items() if k != "title"}}
    return song

new_data = [move_title_first(song) for song in data]

with open("d:/Sandbox/git/aadennis/PythonSandboxAA/MusicHandling/SongbookPro/Instructions/song_metadata.json", "w", encoding="utf-8") as f:
   json.dump(new_data, f, indent=2)