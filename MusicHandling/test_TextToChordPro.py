from TextToChordPro import merge_chords_and_lyrics, process_multiline_text

def test_merge_and_clean():
    chord_line1 = "    Em7         A7        Am         D7"
    lyric_line1 = "Wherever you’re going I’m going your way"

    chord_line2 = "G   Em       C              G"
    lyric_line2 = "Two drifters off to see the world"

    expected1 = "Wher[Em7]ever you’re [A7]going I’m [Am]going your [D7]way"
    expected2 = "[G]Two [Em]drifters [C]off to see the [G]world"

    assert merge_chords_and_lyrics(chord_line1, lyric_line1) == expected1
    assert merge_chords_and_lyrics(chord_line2, lyric_line2) == expected2

def test_multiline_block_with_blank_line():
    input_text1 = '''    Em7         A7        Am         D7
Wherever you’re going I’m going your way
 
G   Em       C              G
Two drifters off to see the world'''

    input_text2 = '''       Bm              C           
Of the bluebird as she sings        
    G          Em               A7     D7       
The sixoclock alarm would never ring
'''

    expected_output1 = [
        "Wher[Em7]ever you’re [A7]going I’m [Am]going your [D7]way",
        "",
        "[G]Two [Em]drifters [C]off to see the [G]world"
    ]

    expected_output2 = [
        "Of the [Bm]bluebird as she [C]sings",        
        "The [G]sixoclock a[Em]larm would never [A7]ring [D7]"
    ]

    result1 = process_multiline_text(input_text1)
    assert result1 == expected_output1

    result2 = process_multiline_text(input_text2)
    assert result2 == expected_output2

