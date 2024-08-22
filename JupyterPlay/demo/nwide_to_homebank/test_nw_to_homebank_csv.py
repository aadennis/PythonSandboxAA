import unittest
import pandas as pd
from nw_to_homebank_csv import preprocess_data

class TestPreprocessData(unittest.TestCase):
    def setUp(self):
        # Sample input data
        input_data = {
            "Date": ["01 Jan 2022", "02 Feb 2022"],
            "Transactions": ["Purchase A", "Purchase B"],
            "Location": ["London", "Manchester"],
            "Paid out": ["£100.00", "£50.00"],
            "Paid in": ["£0.00", "£10.00"],
        }
        self.input_df = pd.DataFrame(input_data)

    def test_preprocess_data(self):
        expected_output = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-02-02"]),
            "payment type": [1, 1],
            "info": ["info 1", "info 1"],
            "Transactions": ["Purchase A", "Purchase B"],
            "Location": ["London", "Manchester"],
            "Paid out": ["100.00", "50.00"],
            "Paid in": ["0.00", "10.00"],
            "category": ["category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2"],
        })

        actual_output = preprocess_data(self.input_df)

        # Compare DataFrames
        pd.testing.assert_frame_equal(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()
