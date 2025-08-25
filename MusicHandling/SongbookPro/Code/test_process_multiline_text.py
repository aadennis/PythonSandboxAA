import pytest
from unittest.mock import patch

# Sample input and expected output
sample_input = """Verse
C       G       Am
This is the first line
Chorus

F       C
Another part begins"""

expected_output = [
    "Verse 1",  # assuming match_and_replace_section returns "Verse 1"
    "C       G       Am",
    "This is the first line",  # merged output mocked
    "Chorus",  # assuming match_and_replace_section returns "Chorus"
    "F       C",
    "Another part begins"  # merged output mocked
]

@pytest.fixture
def mock_match_and_replace_section():
    def _mock(line, section, numbered=False):
        if line == section:
            return f"{section} 1" if numbered else section
        return None
    return _mock

@pytest.fixture
def mock_merge_chords_and_lyrics():
    def _mock(chords, lyrics):
        return lyrics  # Simplified mock: just return lyrics for test
    return _mock

def test_process_multiline_text(mock_match_and_replace_section, mock_merge_chords_and_lyrics):
    with patch("TextToChordPro.match_and_replace_section", side_effect=mock_match_and_replace_section), \
         patch("TextToChordPro.merge_chords_and_lyrics", side_effect=mock_merge_chords_and_lyrics):
        from TextToChordPro import process_multiline_text
        result = process_multiline_text(sample_input)
        assert result == expected_output

