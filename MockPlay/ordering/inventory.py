class Inventory:
    def __init__(self):
        self.stock = {
            'widget': 10,
            'gadget': 5,
            'doodad': 0
        }

    def get_stock(self, item, requested_amount):
        available = self.stock.get(item, 0)
        return available >= requested_amount