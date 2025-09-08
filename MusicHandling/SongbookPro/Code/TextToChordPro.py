# Processes a text file containing chords and lyrics of an 
# UltimateGuitar format, merging them into a format suitable for SongBookPro.
# That format is ChordPro, which is a text-based format for chord sheets.

import os
import json
import re
import zipfile

def merge_chords_and_lyrics(chord_line, lyric_line):
    """
    Merges chords and lyrics into a single line in ChordPro format.

    Args:
        chord_line (str): The line containing chords.
        lyric_line (str): The line containing lyrics.

    Returns:
        str: A single line with chords embedded in the lyrics.
    """
    chord_positions = []
    # Identify positions of chords in the chord line
    for index, char in enumerate(chord_line):
        if char.strip():  # Check if the character is not whitespace
            if index == 0 or chord_line[index - 1] == ' ':
                chord_positions.append(index)

    output = ""
    chord_index = 0
    i = 0

    # Merge chords into the lyrics line
    while i < len(lyric_line):
        if chord_index < len(chord_positions) and i == chord_positions[chord_index]:
            j = chord_positions[chord_index]
            chord = ''
            while j < len(chord_line) and chord_line[j] != ' ':
                chord += chord_line[j]
                j += 1
            output += f"[{chord}]"  # Embed the chord in square brackets
            chord_index += 1
        output += lyric_line[i]
        i += 1

    return clean_spacing(output)

def clean_spacing(line):
    """
    Cleans up extra spaces between words or chords.

    Args:
        line (str): The line to clean.

    Returns:
        str: The cleaned line.
    """
    return re.sub(r'(?<=\S) {2,}(?=\S)', ' ', line)

def match_and_replace_section(line, section_name, numbered=False):
    """
    Checks if the line matches a section header like [Chorus], [Intro], etc.,
    and replaces it with a ChordPro-style section header.

    Args:
        line (str): The line to check.
        section_name (str): The name of the section (e.g., "Chorus").
        numbered (bool): Whether the section can have a number (e.g., "Verse 1").

    Returns:
        str or None: The replacement string if matched, else None.
    """
    if numbered:
        pattern = rf"\[{section_name}(?:\s*\d+)?\]"
    else:
        pattern = rf"\[{section_name}\]"
    if re.match(pattern, line, re.IGNORECASE):
        return f"{{{section_name}}}"
    return None

def process_multiline_text(input_text):
    """
    Processes multiline text, converting it into ChordPro format.

    Args:
        input_text (str): The input text containing chords and lyrics.

    Returns:
        list: A list of lines in ChordPro format.
    """
    lines = [line.rstrip('\n') for line in input_text.splitlines()]
    output_lines = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Replace section headers with ChordPro-style headers
        for section, numbered in [
            ("Verse", True),
            ("Chorus", False),
            ("Intro", False),
            ("Outro", False),
            ("Solo", False),
            ("Bridge", False),
        ]:
            replacement = match_and_replace_section(line, section, numbered=numbered)
            if replacement:
                output_lines.append(replacement)
                i += 1
                # Skip a blank line immediately after a section header
                if i < len(lines) and lines[i].strip() == "":
                    i += 1
                break
        else:
            if not line:
                output_lines.append("")
                i += 1
                continue

            # Merge chords and lyrics if both lines are present
            if i + 1 < len(lines) and lines[i + 1].strip():
                chord_line = lines[i]
                lyric_line = lines[i + 1]

                # Left-align lyric line to match length of chord line
                if len(lyric_line) < len(chord_line):
                    lyric_line = lyric_line.ljust(len(chord_line))

                merged = merge_chords_and_lyrics(chord_line, lyric_line).rstrip()
                output_lines.append(merged)
                i += 2
            else:
                output_lines.append(lines[i].rstrip())
                i += 1

    return output_lines


def to_songbookpro(title, artist, key, capo, tempo, lyrics_lines):
    """
    Converts song metadata and lyrics into SongBookPro format.

    Args:
        title (str): The song title.
        artist (str): The artist name.
        key (str): The song key.
        capo (int): The capo position.
        tempo (int): The tempo of the song.
        lyrics_lines (list): The lyrics in ChordPro format.

    Returns:
        str: The song in SongBookPro format.
    """
    header = [
        f"{{title: {title}}}",
        f"{{artist: {artist}}}",
        f"{{key: {key}}}",
        f"[capo: {capo}]",
        f"{{tempo: {tempo}}}",
        ""
    ]
    return "\n".join(header + lyrics_lines)

def camel_case_to_title(name):
    """
    Converts a CamelCase string to a title with spaces.

    Args:
        name (str): The CamelCase string.

    Returns:
        str: The title with spaces.
    """
    base = os.path.splitext(os.path.basename(name))[0]
    title = re.sub(r'(?<!^)(?=[A-Z])', ' ', base)
    return title.strip()

def get_song_metadata(song):
    """
    Returns the metadata for a song, or creates a default metadata file if not found.

    Args:
        song (str): The song name.

    Returns:
        dict: The metadata for the song.
    """
    metadata_path = os.path.join('Metadata', f"{song}.json")
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Create a default metadata JSON file for the song
        default_metadata = {
            "title": camel_case_to_title(song),
            "artist": "unknown",
            "key-original": "C",
            "key-me": "C",
            "capo": 0,
            "tempo": 88,
            "scroll_speed": 2.7,
            "output_folder": "ChordPro"
        }
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(default_metadata, f, indent=2)
        print(f"Metadata for song '{song}' not found. Default metadata file created at {metadata_path}.")
        return default_metadata

def process_song(song):
    """
    Processes a single song, converting it to ChordPro format.

    Args:
        song (str): The song name.
    """
    # Load all metadata from consolidated song_metadata.json
    metadata_path = os.path.join('Metadata', 'song_metadata.json')
    with open(metadata_path, 'r', encoding='utf-8') as f:
        all_metadata = json.load(f)

    # Find the metadata for the requested song
    song_meta = next((m for m in all_metadata if m.get("title") == song), None)
    if not song_meta:
        # Create a default metadata JSON file for the song
        song_meta = get_song_metadata(song)

    raw_title = song_meta.get("title") or camel_case_to_title(song)
    # If the title contains whitespace, use as-is; else, split on caps
    if " " in raw_title:
        title = raw_title
    else:
        title = re.sub(r'(?<!^)(?=[A-Z])', ' ', raw_title).strip()

    artist = song_meta.get("artist", "")
    key = song_meta.get("key-me", "") or song_meta.get("key", "")
    capo = int(song_meta.get("capo", 0))
    tempo = song_meta.get("tempo", "")
    output_folder = song_meta.get("output_folder", "ChordPro")

    lyrics_file = os.path.join('RawLyricsIn', f"{song}.txt")
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    output_lines = process_multiline_text(input_text)
    songbook_text = to_songbookpro(
        title=title,
        artist=artist,
        key=key,
        capo=capo,
        tempo=tempo,
        lyrics_lines=output_lines
    )

    output_file = os.path.join(output_folder, f"{song}.chordpro")
    os.makedirs(output_folder, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(songbook_text)

def process_all_songs():
    """
    Processes all songs in the RawLyricsIn folder.
    """
    lyrics_folder = 'RawLyricsIn'
    for filename in os.listdir(lyrics_folder):
        if filename.endswith('.txt'):
            song = os.path.splitext(filename)[0]
            process_song(song)

def zip_chordpro_files(zip_name="AllChordProFiles.zip", root_folder="ChordPro"):
    """
    Zips all .chordpro files into a single archive for easy transfer.

    Args:
        zip_name (str): The name of the zip file.
        root_folder (str): The folder containing .chordpro files.
    """
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, _, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith(".chordpro"):
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, root_folder)
                    zipf.write(filepath, arcname)
    print(f"✅ All .chordpro files zipped into '{zip_name}'.")


# Example usage:
if __name__ == "__main__":
    # Uncomment the following line to process a single song
    # process_song("TakeMeHomeCountryRoads")
    
    # Process all songs and zip them
    process_all_songs()
    zip_chordpro_files()


