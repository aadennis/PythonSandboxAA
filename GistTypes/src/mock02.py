# https://docs.python.org/3/library/unittest.mock.html#quick-guide
from unittest.mock import patch

class ClassName2:
    def a(self):
        return 22

class ClassName1:
    def b(self):
        return 33
    
@patch.object(ClassName2, 'a')
@patch.object(ClassName1, 'b')
def test(mock_method):
    ClassName1()
    ClassName2()
    assert MockClass1 is ClassName1
    assert MockClass2 is ClassName2
    assert MockClass1.called
    assert MockClass2.called

test()

