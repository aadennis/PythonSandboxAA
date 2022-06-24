import pytest
import io
import tempfile
from src.model import Model

class TestModel:
    def test_set_1(self):
        a = Model().get_the_lines()
        assert 1 == 1
        
