# Given a ChordPro file, this script converts it back to a format suitable for Ultimate Guitar.
# Normally you would have a UG as the source, but not always.


import sys
import os
import re

def chordpro_to_chord_lyrics(line):
    chord_line = ""
    lyric_line = ""
    i = 0
    while i < len(line):
        if line[i] == "[":
            end = line.find("]", i)
            if end != -1:
                chord = line[i+1:end]
                # Place chord at current position in chord_line
                chord_line += " " * (len(lyric_line) - len(chord_line))
                chord_line += chord
                i = end + 1
            else:
                lyric_line += line[i]
                i += 1
        else:
            lyric_line += line[i]
            i += 1
    chord_line += " " * (len(lyric_line) - len(chord_line))
    return chord_line.rstrip(), lyric_line.rstrip()

def process_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()[5:]  # Skip the first 5 lines (metadata)

    output_lines = []
    for line in lines:
        line = line.rstrip('\n')
        # Replace {c: Verse} and {c: Chorus} with [Verse] and [Chorus]
        if line.strip() == "{c: Verse}":
            output_lines.append("[Verse]")
            continue
        elif line.strip() == "{c: Chorus}":
            output_lines.append("[Chorus]")
            continue
        elif line.strip() == "{Bridge}":
            output_lines.append("[Bridge]")
            continue
        
        chords, lyrics = chordpro_to_chord_lyrics(line)
        if chords.strip():
            output_lines.append(chords)
        # Left strip any whitespace from the lyric line before writing
        output_lines.append(lyrics.lstrip())

    return "\n".join(output_lines)

def get_input_output_files(input_file):
    """
    Returns the input file (with .chordpro extension if missing)
    and the output file path with .ult extension.
    """
    base, ext = os.path.splitext(input_file)
    if not ext:
        input_file += ".chordpro"
        ext = ".chordpro"
    output_file = base + ".txt"
    return input_file, output_file

def convert_chordpro_to_ult(input_file):
    input_file, output_file = get_input_output_files(input_file)
    output = process_file(input_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"Converted file written to: {output_file}")

if __name__ == "__main__":
    input_file = r"D:\onedrive\Music\MusicMaking\SongbookPro\songs\BrowneyedGirl.cho"
    convert_chordpro_to_ult(input_file)