class OrderManagement:
    """
    A class to manage orders and interact with an inventory system.

    Attributes:
        inventory (object): An object representing the inventory system. It is expected to have a `get_stock` method.
        orders (list): A list to store orders. Each order is represented as a dictionary containing customer name, item, and item count.

    Methods:
        __init__(inventory):
            Initializes the OrderManagement instance with the given inventory object.

        place_order(customer_name, item, item_count):
            Places an order for a customer if the requested item and quantity are available in the inventory.
    """

    def __init__(self, inventory):
        """
        Initializes the OrderManagement instance.

        Args:
            inventory (object): An object representing the inventory system. It should have a `get_stock` method to check item availability.
        """
        self.inventory = inventory
        self.orders = []

    def place_order(self, customer_name, item, item_count):
        """
        Places an order for a customer.

        Args:
            customer_name (str): The name of the customer placing the order.
            item (str): The name of the item to be ordered.
            item_count (int): The quantity of the item to be ordered.

        Returns:
            bool: True if the order was successfully placed (item is in stock), False otherwise.
        """
        if self.inventory.get_stock(item, item_count):
            self.orders.append({
                'customer': customer_name,
                'item': item,
                'count': item_count
            })
            return True

