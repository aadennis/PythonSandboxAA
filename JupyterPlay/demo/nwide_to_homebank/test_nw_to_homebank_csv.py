# python -m unittest -v test_module
import unittest
import pandas as pd
from pprint import pprint
from nw_to_homebank_csv import preprocess_data, add_transaction_info, handle_special_payees

class TestPreprocessData(unittest.TestCase):
    def setUp(self):
        # Sample input data
        nw_src_data = {
            "Date": ["01 Jan 2022", "31 Jan 2022", "02 Feb 2022"],
            "Transactions": ["PURCHASE ax", "PurCHAse b", "purchase c"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["£100.00", "", "£254.23"],
            "Paid in": ["", "£10.00", ""]
        }
       
        # Amazon.co.uk*HB8CO4G74
        nw_imported_data = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31", "2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["info 1", "info 1", "info 1"],
            "Transactions": ["Purchase A", "Purchase B", "Purchase C"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00", ""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })
        nw_amazon_data = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31", "2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["info 1", "info 1", "info 1"],
            "Transactions": ["AmaZOn.co.uk*HB8CO4G74", "AMZNMktplace", "Purchase C"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00", ""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })
        amazon_capped_data = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31", "2022-02-02", "2024-02-02"]),
            "payment type": [1, 1, 1,1],
            "info": ["info 1", "info 1", "info 1", "info 1"],
            "Transactions": ["Amazon.co.uk*hb8co4g74", "Amznmktplace", "Www.amazon* 204-33", "DIRECT DEBIT PAYMENT"],
            "Location": ["London", "Manchester", "London", "Chicago"],
            "Paid out": ["100.00", "", "254.23", "2030.34"],
            "Paid in": ["", "10.00", "", ""],
            "category": ["category 1", "category 1", "category 1", "snood farm"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2", "tag3 tag4"],
        })

        self.input_df = pd.DataFrame(nw_src_data)
        self.nw_imported_data = pd.DataFrame(nw_imported_data)
        self.nw_amazon_data = pd.DataFrame(nw_amazon_data)
        self.amazon_capped_data = pd.DataFrame(amazon_capped_data)
        
    #@unittest.skip('Work in progress')
    def test_preprocess_data(self):
        expected_output = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31", "2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["info 1", "info 1", "info 1"],
            "Transactions": ["Purchase ax", "Purchase b", "Purchase c"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00", ""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })

        actual_output = preprocess_data(self.input_df)

        # Compare DataFrames
        pd.testing.assert_frame_equal(expected_output, actual_output)

    #@unittest.skip('Work in progress')
    def test_first_last_in_statement(self):
        expected_output = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31", "2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["First transaction in statement", "info 1", "Last transaction in statement"],
            "Transactions": ["Purchase A", "Purchase B", "Purchase C"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00", ""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })

        actual_output = add_transaction_info(self.nw_imported_data)

        pd.testing.assert_frame_equal(expected_output, actual_output)

    def test_lcase_for_txns(self):
        expected_output = pd.DataFrame({
            "Date": pd.to_datetime(["2022-01-01", "2022-01-31", "2022-02-02"]),
            "payment type": [1, 1, 1],
            "info": ["info 1", "info 1", "info 1"],
            "Transactions": ["Amazon.co.uk*hb8co4g74", "Amznmktplace", "Purchase c"],
            "Location": ["London", "Manchester", "London"],
            "Paid out": ["100.00", "", "254.23"],
            "Paid in": ["", "10.00", ""],
            "category": ["category 1", "category 1", "category 1"],
            "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2"],
        })


        actual_output = preprocess_data(self.nw_amazon_data)
        pd.testing.assert_frame_equal(expected_output, actual_output)


    def test_special_payees(self):
            expected_output = pd.DataFrame({
                "Date": pd.to_datetime(["2022-01-01", "2022-01-31", "2022-02-02", "2024-02-02"]),
                "payment type": ["1", "1", "1", "11"],
                "info": ["info 1", "info 1", "info 1", "info 1"],
                "Transactions": ["Amazon", "Amazon", "Amazon", "DIRECT DEBIT PAYMENT"],
                "Location": ["London", "Manchester", "London", "Chicago"],
                "Paid out": ["100.00", "", "254.23", "2030.34"],
                "Paid in": ["", "10.00", "", ""],
                "category": ["category 1", "category 1", "category 1", "snood farm"],
                "Tags": ["tag1 tag2", "tag1 tag2", "tag1 tag2", "tag3 tag4"],
            })
            pprint(self.amazon_capped_data)
            actual_output = handle_special_payees(self.amazon_capped_data)
            pprint(actual_output)
            pd.testing.assert_frame_equal(expected_output, actual_output)

        
if __name__ == "__main__":
    unittest.main()
