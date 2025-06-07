# This script processes a text file containing chords and lyrics of an 
# UltimateGuitar format, merging them into a format suitable for SongBookPro.

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

    return output

def process_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]

    with open(output_file, "w", encoding="utf-8") as out:
        for i in range(0, len(lines) - 1, 2):
            chord_line = lines[i]
            lyric_line = lines[i+1]
            merged = merge_chords_and_lyrics(chord_line, lyric_line)
            out.write(merged + "\n")

# Example usage:
if __name__ == "__main__":
    process_file("MoonRiverIn.txt", "MoonRiverOut.txt")


