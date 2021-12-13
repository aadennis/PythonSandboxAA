"""
To execute tests from command line, go to the parent of folders 
    src and test, and run:
    pytest.exe test -v
"""
from Utilities.src.utility import Utility
import unittest


class ParseIntTestCase(unittest.TestCase):
    
    def test_is_true_if_input_is_int(self):
        util = Utility()
        result = util.parse_int('33')
        self.assertEqual(result, True)

    def test_is_false_if_input_is_float(self):
        util = Utility()
        result = util.parse_int('33.2')
        self.assertEqual(result, False)

class FilesAreSameTestCase(unittest.TestCase):

    def test_is_true_if_files_are_same(self):
        file_1 = "Utilities/test/file1.txt"
        file_2 = "Utilities/test/file1_copy.txt"
        util = Utility()
        result = util.files_are_same(file_1, file_2)
        assert(result)

    def test_is_false_if_files_are_not_same(self):
        file_1 = "Utilities/test/file1.txt"
        file_2 = "Utilities/test/not_file1_copy.txt"
        util = Utility()
        result = util.files_are_same(file_1, file_2)
        assert(not result)