# This script processes a text file containing chords and lyrics of an 
# UltimateGuitar format, merging them into a format suitable for SongBookPro.

import re
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
            # Extract full chord
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
    # Collapse 2+ spaces between visible characters
    # The regular expression (?<=\S) {2,}(?=\S) matches 2 or more spaces between 
    # non-space characters. So it doesn’t touch legitimate spacing between [C] and a word.
    # This keeps alignment OK without crushing [Chord] formatting
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
            merged = merge_chords_and_lyrics(lines[i], lines[i + 1])
            output_lines.append(merged)
            i += 2
        else:
            output_lines.append(lines[i])
            i += 1

    return output_lines

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    output_lines = process_multiline_text(input_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')


# Example usage:
if __name__ == "__main__":
    process_file("MoonRiverIn.txt", "MoonRiverOut.txt")


