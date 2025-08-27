class OrderManagement:
    def __init__(self, inventory):
        self.inventory = inventory
        self.orders = []

    def place_order(self, customer_name, item, item_count):
        if self.inventory.get_stock(item, item_count):
            self.orders.append({
                'customer': customer_name,
                'item': item,
                'count': item_count
            })
            return True
        else:
            return False
        
