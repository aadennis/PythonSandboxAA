import pytest
import io
import tempfile
from src.tideday import TideDay

class TestTideDay:
    def test_is_valid_tideday_record(self):
        line = "29,0138013,0746407,1401000,2011390"
        td = TideDay(line,3,2022,"low")

        assert td.tide_date == 29
        assert len(td.tide_times) == 4
        assert td.tide_times[0] == "0138013"
        assert td.tide_times[1] == "0746407"
        assert td.tide_times[2] == "1401000"
        assert td.tide_times[3] == "2011390"
        assert td.tide_month == 3
        assert td.tide_type == "low"

    def test_GetFormattedDay(self):
        line = "29,0138013,0746407,1401000,2011390"
        td = TideDay(line,3,2022,"low")

        assert td.GetFormattedDay() == "29/03/2022,4.07,Low,01:38:00,0.13,High,07:46:00,4.07,Low,14:01:00,0.0,High,20:11:00,3.9"

    def test_is_not_valid_tideday_record(self):
        with pytest.raises(ValueError):
            line = "29,a138013,0746407,1401000,2011390"
            td = TideDay(line,1,2022,"low")


   