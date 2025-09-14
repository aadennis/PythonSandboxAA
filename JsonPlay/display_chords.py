import json
import sys

# Load chord data from a JSON file
# The JSON file is expected to contain a list of chord entries, where each entry has a 'chord_id' and a list of 'sa_notes'.
# 'sa_notes' means 'Strummed Acoustic notes', a VST from the Native Instruments collection.
with open('chords2.json', 'r') as f:
    chord_data = json.load(f)

# Build a lookup dictionary to map each chord_id to its corresponding list of notes.
chord_lookup = {
    entry['chord_id']: (entry['name'], [note['sa_note'] for note in entry['sa_notes']])
    for entry in chord_data
}

def display_chords(chord_string):
    """
    Display the notes for a given comma-separated string of chord IDs.

    Args:
        chord_string (str): A comma-separated string of chord IDs (e.g., 'c,c_maj7,c_aug').

    Behavior:
        - For each chord ID in the input string:
            - If the chord ID exists in the lookup dictionary, print the chord ID and its notes.
            - If the chord ID is not found, print an error message and exit the program.
    """
    chords = chord_string.split(',')

    for chord in chords:
        # Check if the chord ID exists in the lookup dictionary
        if chord not in chord_lookup:
            print(f"Chord '{chord}' not found in database.")
            sys.exit(1)  -

        # Retrieve the list of notes for the chord
        name, notes = chord_lookup[chord]

        # Print the chord ID and its notes
        print(f"{chord} ({name})")
        print(','.join(notes))  # Join the notes with commas and print them
        print('-' * 27)  # Print a separator line for better readability

# Example usage of the script
# The input string contains a list of chord IDs to display
input_chords = 'c,c_maj7,c_aug'
display_chords(input_chords)
