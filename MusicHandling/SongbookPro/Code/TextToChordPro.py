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


def to_songbookpro(title, artist, key, capo, tempo, lyrics_lines):
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
    # Remove extension, insert space before each uppercase letter (except first)
    base = os.path.splitext(os.path.basename(name))[0]
    title = re.sub(r'(?<!^)(?=[A-Z])', ' ', base)
    return title.strip()

def process_song(song):
    # Load all metadata from consolidated song_metadata.json
    metadata_path = os.path.join('Metadata', 'song_metadata.json')
    with open(metadata_path, 'r', encoding='utf-8') as f:
        all_metadata = json.load(f)

    # Find the metadata for the requested song
    song_meta = next((m for m in all_metadata if m.get("title") == song), None)
    if not song_meta:
        raise ValueError(f"Metadata for song '{song}' not found in song_metadata.json")

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
    lyrics_folder = 'RawLyricsIn'
    for filename in os.listdir(lyrics_folder):
        if filename.endswith('.txt'):
            song = os.path.splitext(filename)[0]
            process_song(song)

# Example usage:
if __name__ == "__main__":
    #process_song("The Last Thing on my Mind")
    process_all_songs()

