

class Order:
    def __init__(self, order_id, customer_name, mobile_number, order_items, total_order_price, order_date, status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.order_items = order_items
        self.total_order_price = total_order_price
        self.order_date = order_date
        self.status = status

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "mobile_number": self.mobile_number,
            "order_items": self.order_items,
            "total_order_price": self.total_order_price,
            "order_date": self.order_date,
            "status": self.status
        }
