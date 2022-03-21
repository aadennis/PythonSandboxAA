# import pytest
from src.DocumentLine import DocumentLine

class TestDocumentLine:
    def test_1_or_more_words(self):
        """
        1 or more words in a line makes a valid line
        """
        line = DocumentLine("This is a line", 1)
        assert line.is_valid_line()

    def test_zero_words(self):
        """
        zero characters in a line makes a not-valid line
        """
        line = DocumentLine("        ", 1)
        assert not line.is_valid_line()

    def test_empty_string(self):
        """
        an empty string is not a valid line
        """
        line = DocumentLine("", 1)
        assert not line.is_valid_line()

    def test_zero_char_count(self):
        line = DocumentLine("", 1)
        assert line.get_char_count() == 0

    def test_ws_only_char_count(self):
        line = DocumentLine("\n\r", 1)
        assert line.get_char_count() == 0

    def test_many_char_count(self):
        """
        mix of 'true' chars and whitespace
        """
        line = DocumentLine("abc def 2\n\r", 1)
        assert line.get_char_count() == 7