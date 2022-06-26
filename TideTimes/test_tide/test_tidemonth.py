import pytest
import io
import tempfile
from src.tidemonth import TideMonth

class TestTideMonth:
    def test_default_month_year(self):
        tide_month_data = ["Low","#hight"]
        tm = TideMonth(tide_month_data)
        assert tm.month == 6
        assert tm.year == 2022

    def test_tide_type_low(self):
        tide_month_data = ["Low","#hight"]
        tm = TideMonth(tide_month_data)
        assert tm.tide_type == "low"
             
    def test_tide_type_high(self):
        tide_month_data = ["Low","High"]
        tm = TideMonth(tide_month_data)
        assert tm.tide_type == "high"     

    # Note that a misspelled tide type will be interpreted as a bad full
    # record, with insufficient arguments
    # def test_tide_type_none(self):
    #     tide_month_data = ["slow","sHigh"]
    #     tm = TideMonth(tide_month_data)
    #     assert not tm.tide_type

