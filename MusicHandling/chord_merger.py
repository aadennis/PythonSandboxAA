# This script processes a text file containing chords and lyrics of an 
# UltimateGuitar format, merging them into a format suitable for SongBookPro.

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

            # Pad lyric line to match chord line's indentation
            if len(lyric_line) < len(chord_line):
                lyric_line = ' ' * (len(chord_line) - len(lyric_line)) + lyric_line

            merged = merge_chords_and_lyrics(chord_line, lyric_line)
            output_lines.append(merged)
            i += 2
        else:
            output_lines.append(lines[i])
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

def process_file(input_file, output_file_base, title, artist, key, tempo):
    with open(input_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    output_lines = process_multiline_text(input_text)
    songbook_text = to_songbookpro(title, artist, key, tempo, output_lines)

    output_file = f"{output_file_base}.chordpro"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(songbook_text)

# Example usage:
if __name__ == "__main__":
    process_file(
        input_file="out.txt",
        output_file_base="Daydream_Believer",
        title="Daydream Believer",
        artist="Monkees",
        key="G",
        tempo=88
    )
