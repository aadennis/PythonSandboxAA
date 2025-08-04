# Processes a text file containing chords and lyrics of an 
# UltimateGuitar format, merging them into a format suitable for SongBookPro.
# That format is ChordPro, which is a text-based format for chord sheets.

import os
import json
import re

def merge_chords_and_lyrics(chord_line, lyric_line):
    chord_positions = []
    for index, char in enumerate(chord_line):
        if char.strip():
            if index == 0 or chord_line[index - 1] == ' ':
                chord_positions.append(index)

    output = ""
    chord_index = 0
    i = 0

    while i < len(lyric_line):
        if chord_index < len(chord_positions) and i == chord_positions[chord_index]:
            j = chord_positions[chord_index]
            chord = ''
            while j < len(chord_line) and chord_line[j] != ' ':
                chord += chord_line[j]
                j += 1
            output += f"[{chord}]"
            chord_index += 1
        output += lyric_line[i]
        i += 1

    return clean_spacing(output)

def clean_spacing(line):
    return re.sub(r'(?<=\S) {2,}(?=\S)', ' ', line)

def match_and_replace_section(line, section_name, numbered=False):
    """
    Checks if the line matches a section header like [Chorus], [Intro], [Verse], [Verse 1], etc.
    Returns the replacement string (e.g., "{Chorus}") if matched, else None.
    """
    if numbered:
        pattern = rf"\[{section_name}(?:\s*\d+)?\]"
    else:
        pattern = rf"\[{section_name}\]"
    if re.match(pattern, line, re.IGNORECASE):
        return f"{{{section_name}}}"
    return None

def process_multiline_text(input_text):
    lines = [line.rstrip('\n') for line in input_text.splitlines()]
    output_lines = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Section header replacements
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
                # Suppress a blank line immediately after a section header
                if i < len(lines) and lines[i].strip() == "":
                    i += 1
                break
        else:
            if not line:
                output_lines.append("")
                i += 1
                continue

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


def to_songbookpro(title, artist, key, tempo, lyrics_lines):
    header = [
        f"{{title: {title}}}",
        f"{{artist: {artist}}}",
        f"{{key: {key}}}",
        f"{{tempo: {tempo}}}",
        ""
    ]
    return "\n".join(header + lyrics_lines)

def camel_case_to_title(name):
    # Remove extension, insert space before each uppercase letter (except first)
    base = os.path.splitext(os.path.basename(name))[0]
    title = re.sub(r'(?<!^)(?=[A-Z])', ' ', base)
    return title.strip()

def process_file(song):
    instructions_path = os.path.join('Instructions', f"{song}.json")
    lyrics_file = os.path.join('RawLyricsIn', f"{song}.txt")

    # If JSON does not exist, create it with default values
    if not os.path.exists(instructions_path):
        default_metadata = {
            "artist": "unknown",
            "key": "C",
            "tempo": 88,
            "output_folder": "ChordPro"
        }

        with open(instructions_path, 'w', encoding='utf-8') as f:
            json.dump(default_metadata, f, indent=2)

    # Read metadata from JSON
    with open(instructions_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    title = metadata.get("title") or camel_case_to_title(song)
    artist = metadata.get("artist", "")
    key_original = metadata.get("key-original", "")
    key_me = metadata.get("key-me", "")
    
    tempo = metadata.get("tempo", "")
    output_folder = metadata.get("output_folder", "")

    # Read lyrics
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    output_lines = process_multiline_text(input_text)
    songbook_text = to_songbookpro(
        title=title,
        artist=artist,
        key=key_me,
        tempo=tempo,
        lyrics_lines=output_lines
    )

    # Build output file path
    output_file = os.path.join(output_folder, f"{song}.chordpro")
    os.makedirs(output_folder, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(songbook_text)

def process_all_songs():
    lyrics_folder = 'RawLyricsIn'
    instructions_folder = 'Instructions'
    output_folder_default = 'ChordPro'

    for filename in os.listdir(lyrics_folder):
        if filename.endswith('.txt'):
            song = os.path.splitext(filename)[0]
            instructions_path = os.path.join(instructions_folder, f"{song}.json")
            lyrics_file = os.path.join(lyrics_folder, filename)

            # If JSON does not exist, create it with default values
            if not os.path.exists(instructions_path):
                default_metadata = {
                    "artist": "unknown",
                    "key-original": "C",
                    "key-me": "C",
                    "tempo": 88,
                    "output_folder": output_folder_default
                }
                with open(instructions_path, 'w', encoding='utf-8') as f:
                    json.dump(default_metadata, f, indent=2)

            # Read metadata from JSON
            with open(instructions_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)

            title = metadata.get("title") or camel_case_to_title(song)
            artist = metadata.get("artist", "")
            key = metadata.get("key", "")
            tempo = metadata.get("tempo", "")
            output_folder = metadata.get("output_folder", output_folder_default)

            # Read lyrics
            with open(lyrics_file, 'r', encoding='utf-8') as f:
                input_text = f.read()

            output_lines = process_multiline_text(input_text)
            songbook_text = to_songbookpro(title, artist, key, tempo, output_lines)

            # Build output file path
            output_file = os.path.join(output_folder, f"{song}.chordpro")
            os.makedirs(output_folder, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(songbook_text)

# Example usage:
if __name__ == "__main__":
    #process_file(song="AHardDaysNight")
    process_all_songs()

