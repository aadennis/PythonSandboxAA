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

def process_multiline_text(input_text):
    lines = [line.rstrip('\n') for line in input_text.splitlines()]
    output_lines = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()
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

def process_file(input_file):
    # Read metadata from JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # Derive title from file name if not present in metadata
    title = camel_case_to_title(input_file)
    artist = metadata.get("artist", "")
    key = metadata.get("key", "")
    tempo = metadata.get("tempo", "")
    output_folder = metadata.get("output_folder", "")

    # Derive lyrics file name
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    lyrics_file = os.path.join(os.path.dirname(input_file), f"{base_name}_lyrics.txt")

    # Read lyrics
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    output_lines = process_multiline_text(input_text)
    songbook_text = to_songbookpro(title, artist, key, tempo, output_lines)

    # Build output file path
    output_file = os.path.join(output_folder, f"{base_name}.chordpro")
    os.makedirs(output_folder, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(songbook_text)

# Example usage:
if __name__ == "__main__":
    process_file(input_file="MoonRiver.json")

