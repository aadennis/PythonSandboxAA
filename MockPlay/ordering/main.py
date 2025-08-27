from inventory import Inventory
from order_management import OrderManagement

if __name__ == '__main__':
    inv = Inventory()
    om = OrderManagement(inventory=inv)

    result = om.place_order('Alice', 'widget', 3)
    print('Order placed:', result)