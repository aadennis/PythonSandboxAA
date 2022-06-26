import pytest
import io
import tempfile
from src.tideday import TideDay

class TestTideDay:
    def test_is_valid_tideday_record(self):
        line = "29,0138013,0746407,1401000,2011390"
        td = TideDay(line,1,"low")

        assert td.get_items() == 29

   