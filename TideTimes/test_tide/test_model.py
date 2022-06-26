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
        line = "hiGh"
        tide_type = Model().get_tide_type(line)
        assert tide_type == 'high'
        
    def test_is_tide_low(self):
        line = "lOw"
        tide_type = Model().get_tide_type(line)
        assert tide_type == 'low'

    def test_is_tide_low2(self):
        line = "lOwAtLeastTheFirstCharsMatch"
        tide_type = Model().get_tide_type(line)
        assert tide_type == 'low'

    def test_is_not_tide(self):
        line = "None of these"
        tide_type = Model().get_tide_type(line)
        assert tide_type == None

    def test_is_data_record(self):
        line = "7,The rest"
        tide_date = Model().get_tide_day(line)
        assert tide_date == 7

    def test_is_not_data_record(self):
        line = "73,The rest"
        tide_date = Model().get_tide_day(line)
        assert tide_date == None

    def test_is_not_data_record_2(self):
        line = "x,The rest"
        tide_date = Model().get_tide_day(line)
        assert tide_date == None
