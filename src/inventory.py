"""inventory module"""
class Inventory:
    """define inventories for characters and containers"""
    def __init__(self):
        self.container = []
    def add_item(self,item):
        """add and item to this inventory"""
        self.container.append(item)
