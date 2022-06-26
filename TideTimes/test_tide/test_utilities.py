import pytest
import io
import tempfile
from src.utilities import Utilities

class TestUtilities:
    def test_get_tidal_range(self):
        items = ["0138013","0746407","1401000","2011390"]
        
        tidal_range = Utilities().get_tidal_range2(items)

        # Given the test data, this is the difference between
        # the min 0.00 and the max 4.07
        assert tidal_range == 4.07

    def test_get_tide_position_low(self):
        first_tide = "low"
        for i in range(0,4):
            tide_type = Utilities().get_tide_position(first_tide, i)
            assert tide_type == Utilities.LOW_TIDE_FIRST[i]

    def test_get_tide_position_high(self):
        first_tide = "high"
        for i in range(0,4):
            tide_type = Utilities().get_tide_position(first_tide, i)
            assert tide_type == Utilities.HIGH_TIDE_FIRST[i]

    def test_get_tide_instance2(self):
        first_tide = True # meaning first tide is high

        for index in range(0,4):
            tide_type = Utilities().get_tide_instance2(index, first_tide, "1903445")
            if index%2 == 0:
                assert tide_type == "High,19:03:00,4.45"
            else:
                assert tide_type == "Low,19:03:00,4.45"