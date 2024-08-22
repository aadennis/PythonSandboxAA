import unittest
import pandas as pd
from nw_to_homebank_csv import preprocess_data, add_transaction_info

class TestPreprocessData(unittest.TestCase):
    def setUp(self):
        # Sample input data
        nw_src_data = {
            "Date": ["01 Jan 2022", "31 Jan 2022", "02 Feb 2022"],
            "Transactions": ["Purchase A", "Purchase B", "Purchase C"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["£100.00", "","£254.23"],
            "Paid in": ["", "£10.00", ""]
        }
        nw_imported_data = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31","2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["info 1", "info 1","info 1"],
            "Transactions": ["Purchase A", "Purchase B", "Purchase C"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00",""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })
        self.input_df = pd.DataFrame(nw_src_data)
        self.nw_imported_data = pd.DataFrame(nw_imported_data)


    def test_preprocess_data(self):
        expected_output = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31","2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["info 1", "info 1","info 1"],
            "Transactions": ["Purchase A", "Purchase B", "Purchase C"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00",""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })

        actual_output = preprocess_data(self.input_df)

        # Compare DataFrames
        pd.testing.assert_frame_equal(expected_output, actual_output)

    def test_first_last_in_statement(self):
        expected_output = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31","2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["First transaction in statement", "info 1","Last transaction in statement"],
            "Transactions": ["Purchase A", "Purchase B", "Purchase C"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00",""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })

        actual_output = add_transaction_info(self.nw_imported_data)

        pd.testing.assert_frame_equal(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()
