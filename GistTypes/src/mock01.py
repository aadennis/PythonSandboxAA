# https://docs.python.org/3/library/unittest.mock.html#quick-guide
from unittest.mock import MagicMock

class ProductionClass: 
    def method(self, a,b,c, key):
        return 22


thing = ProductionClass()
thing.method = MagicMock(return_value=3)
a = thing.method(3,4,5,key='value')
print(a)
thing.method.assert_called_with(3, 4, 5, key='value')