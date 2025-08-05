import sys

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
        lines = f.readlines()

    output_lines = []
    for line in lines:
        line = line.rstrip('\n')
        chords, lyrics = chordpro_to_chord_lyrics(line)
        if chords.strip():
            output_lines.append(chords)
        output_lines.append(lyrics)

    return "\n".join(output_lines)

if __name__ == "__main__":
    input_file = "ChordPro/ImABeliever"
    output = process_file(input_file)
    print(output)