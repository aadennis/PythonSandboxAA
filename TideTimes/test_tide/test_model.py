import pytest
import io
import tempfile
from src.model import Model

class TestModel:
    def test_is_comment_line(self):
        line = "# this is a comment"
        is_comment = Model().is_comment_line(line)
        assert is_comment == True

    def test_is_data_line(self):
        line = "Any line that does not start with # is data"
        is_comment = Model().is_comment_line(line)
        assert is_comment == False

    def test_is_tide_high(self):
        line = "lOw"
        is_tide = Model().is_tide(line)
        assert is_tide

    def test_is_tide_low(self):
        line = "hIGh"
        is_tide = Model().is_tide(line)
        assert is_tide

    def test_data_is_not_tide(self):
        line = "xhIGh"
        is_tide = Model().is_tide(line)
        assert not is_tide
        
