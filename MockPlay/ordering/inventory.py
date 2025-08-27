class Inventory:
    """
    A class to manage and track the stock of items in an inventory.

    Attributes:
        stock (dict): A dictionary representing the inventory stock. Keys are item names (str), 
        and values are their quantities (int).

    Methods:
        __init__():
            Initializes the Inventory instance with predefined stock levels.

        get_stock(item, requested_amount):
            Checks if the requested amount of an item is available in the inventory.
    """

    def __init__(self):
        """
        Initializes the Inventory instance with predefined stock levels.
        """
        self.stock = {
            'widget': 10,
            'gadget': 5,
            'doodad': 0
        }

    def get_stock(self, item, requested_amount):
        """
        Checks if the requested amount of an item is available in the inventory.

        Args:
            item (str): The name of the item to check.
            requested_amount (int): The quantity of the item being requested.

        Returns:
            bool: True if the requested amount is available, False otherwise.
        """
        available = self.stock.get(item, 0)
        return available >= requested_amount