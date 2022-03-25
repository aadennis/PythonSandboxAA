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
        """
        an empty string means zero char count
        """
        line = DocumentLine("", 1)
        assert line.get_char_count() == 0

    def test_ws_only_char_count(self):
        """
        whitespace-only means zero char count
        """
        line = DocumentLine("\n\r", 1)
        assert line.get_char_count() == 0

    def test_many_char_count(self):
        """
        mix of 'true' chars and whitespace
        """
        line = DocumentLine("abc def 2\n\r", 1)
        assert line.get_char_count() == 7

    def test_word_count_many(self):
        line = DocumentLine("one two three 4", 1)
        assert line.get_word_count() == 4

    def test_word_count_zero(self):
        line = DocumentLine("   ", 1)
        assert line.get_word_count() == 0

    def test_word_count_1word(self):
        line = DocumentLine(" jasmine ", 1)
        assert line.get_word_count() == 1

    def test_header_line_has_0_words(self):
        line = DocumentLine(" \n", 1)
        assert line.is_header() is False
        
    def test_header_line_has_1_word(self):
        line = DocumentLine(" Jasmine \n", 1)
        assert line.is_header() is True

    def test_header_line_has_lt_max_words(self):
        line = DocumentLine("Jasmine and other flowers are tasty\n", 1)
        assert line.is_header() is True

    def test_header_line_has_gt_max_words(self):
        # 12 words
        line = DocumentLine("Jasmine and other flowers are tasty but not as much as chocolate \n", 1)
        assert line.is_header() is False

    def test_header_line_has_eq_max_words(self):
        # 10 words
        line = DocumentLine("Other flowers are tasty but not as much as chocolate \n", 1)
        assert line.is_header() is True

    def test_paragraph_style_is_none(self):
        line = DocumentLine("\r\n", 1)
        assert line.get_paragraph_type() == None

    def test_paragraph_style_is_header(self):
        line = DocumentLine("A header thing \n", 1)
        assert line.get_paragraph_type() == "Header"

    def test_paragraph_style_is_body(self):
        line = DocumentLine("Jasmine and other flowers are tasty but not as much as chocolate \n", 1)
        assert line.get_paragraph_type() == "Body"

    def test_get_line(self):
        line = DocumentLine("Jasmine and other weeds",1)
        assert line.get_line() == "Jasmine and other weeds"

    def test_get_lineindex(self):
        line = DocumentLine("Some weeds",22)
        assert line.get_lineindex() == 22

