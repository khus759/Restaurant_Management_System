import uuid
import datetime

class Bill:
    GST_RATE = 0.18

    def __init__(self, order):
        # Using a predefined namespace and order ID to create a deterministic UUID
        self.billing_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(order.order_id)))[:6]
        self.order_id = order.order_id
        self.customer_name = order.customer_name
        self.billing_date = datetime.datetime.now().strftime("%d-%b-%Y %I:%M:%p")
        self.items = order.order_items
        self.subtotal = order.total_order_price
        self.gst = self.subtotal * Bill.GST_RATE
        self.total = self.subtotal + self.gst
        self.status = "Billed"
        self.payment_type = None
        self.payment_date = None
        self.user_email = order.user_email



    def to_dict(self):
        return {
            "billing_id": self.billing_id,
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "billing_date": self.billing_date,
            "items": self.items,
            "subtotal": self.subtotal,
            "gst": self.gst,
            "total": self.total,
            "status": self.status,
            "payment_type": self.payment_type,
            "payment_date": self.payment_date,
            "user_email":self.user_email
        }
