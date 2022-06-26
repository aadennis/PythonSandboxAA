import pytest
import io
import tempfile
from src.tideday import TideDay

class TestTideDay:
    def test_is_valid_tideday_record(self):
        line = "29,0138013,0746407,1401000,2011390"
        td = TideDay(line,1,"low")

        assert td.tide_date == 29
        assert len(td.tide_times) == 4
        assert td.tide_times[0] == "0138013"
        assert td.tide_times[1] == "0746407"
        assert td.tide_times[2] == "1401000"
        assert td.tide_times[3] == "2011390"

    def test_is_not_valid_tideday_record(self):
        line = "29,a138013,0746407,1401000,2011390"
        td = TideDay(line,1,"low")


   