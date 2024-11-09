class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "item id": self.item_id,
            "item name": self.name,
            "price": self.price
        }
    
    