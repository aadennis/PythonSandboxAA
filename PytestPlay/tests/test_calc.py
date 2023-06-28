from src import calc

def test_add():
    assert(calc.add(1,2) == 3)

def test_subtract():
    assert(calc.subtract(10,6) == 4)