import unittest
from unittest.mock import MagicMock
from inventory import Inventory
from order_management import OrderManagement

class TestOrderManagement(unittest.TestCase):
    def test_place_order_success(self):
        mock_inventory = MagicMock(autospec=Inventory)
        mock_inventory.get_stock.return_value = True

        om = OrderManagement(mock_inventory)
        result = om.place_order('Alice', 'widget', 3)

        self.assertTrue(result)
        self.assertEqual(len(om.orders), 1)
        self.assertEqual(om.orders[0]['customer'], 'Alice')

    def test_typo_in_method_name(self):
        mock_inventory = MagicMock(autospec=Inventory)
        # This will raise AttributeError because get_stockx doesn't exist
        with self.assertRaises(AttributeError):
            mock_inventory.get_stockx = MagicMock(return_value=True)

    def test_place_order_failure(self):
        mock_inventory = Inventory()
        mock_inventory.get_stock = MagicMock(return_value=False)

        om = OrderManagement(mock_inventory)
        result = om.place_order('Bob', 'doodad', 2)

        self.assertFalse(result)
        self.assertEqual(len(om.orders), 0)

if __name__ == '__main__':
    unittest.main()

