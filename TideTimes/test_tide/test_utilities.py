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




   