import pytest
import io
import tempfile
from src.tidemonth import TideMonth

from pathlib import Path 


class TestTideMonth:
    def test_default_month_year(self):
        tide_month_data = ["Low","#hight"]
        tm = TideMonth(tide_month_data, 6)
        assert tm.month == 6
        assert tm.year == 2022

    def test_tide_type_low(self):
        tide_month_data = ["Low","#hight"]
        tm = TideMonth(tide_month_data, 6)
        assert tm.tide_type == "low"
             
    def test_tide_type_high(self):
        tide_month_data = ["Low","High"]
        tm = TideMonth(tide_month_data, 6)
        assert tm.tide_type == "high"

    def test_1day_tide(self):
        tide_month_data = ["Low","# just a comment", 
        "29,0338013,0746407,1401000,2011390"]
        tm = TideMonth(tide_month_data, 6)
        tm_result = tm.get_formatted_tide_month()
        assert tm_result[0] == "29/06/2022,4.07,Low,03:38:00,0.13,High,07:46:00,4.07,Low,14:01:00,0.0,High,20:11:00,3.9"

    def test_tide_change(self):
        tide_month_datax = [
            "Low","# just a comment", 
            "3,0138013,0746407,1401000,2011390",
            "4,0148015,0846407,1501020,2031410",
            "High",
            "5,0158015,0855407,1504020,2031415",
            ]
        tm = TideMonth(tide_month_datax, 6)
        tm_results = tm.get_formatted_tide_month()
        assert tm_results[0] == "03/06/2022,4.07,Low,01:38:00,0.13,High,07:46:00,4.07,Low,14:01:00,0.0,High,20:11:00,3.9"

    def test_read_monthfile(self):
        print("File Path:", Path(__file__).absolute()) 
        root = Path().absolute()
        print("Directory Path:", Path().absolute()) # Directory of current working directory, not __file__

        tide_month_data =[]

        file_path =  "test_tide/data/tidetimes_2022_04_v2_dictated.csv"
        with io.open(file_path, 'r') as f:
            for line in f:
                tide_month_data.append(line)
        tm = TideMonth(tide_month_data, 6)
        tm_results = tm.get_formatted_tide_month()
        for e,i in enumerate(tm_results):
            print(i)
        assert 1 == 2

    # Note that a misspelled tide type will be interpreted as a bad full
    # record, with insufficient arguments
    # def test_tide_type_none(self):
    #     tide_month_data = ["slow","sHigh"]
    #     tm = TideMonth(tide_month_data)
    #     assert not tm.tide_type

