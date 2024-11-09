import os
import json
from datetime import datetime
from uuid import uuid4

MENU_FILE = 'Src/Database/menu.json'
ORDER_FILE = 'Src/Database/order.json'

class Menu:
    def __init__(self, filename):
        self.filename = filename
        self.items = self.load_menu()

    def load_menu(self):
        with open(self.filename, 'r') as file:
            return json.load(file)[0]

    def display(self):
        print("Menu:")
        for category, items in self.items.items():
            print(f"\n{category}:")
            for item in items:
                print(f"ID: {item['item id']}, Name: {item['item name']}, Price: {item['price']}")

class Order:
    def __init__(self, customer_name, customer_mobile, items):
        name_prefix = customer_name[::2].upper()
        self.order_id = f"{name_prefix}{str(uuid4())[:4]}"
        self.customer_name = customer_name
        self.customer_mobile = customer_mobile
        self.timestamp = datetime.now().strftime('%d-%b-%Y %I:%M:%p')
        self.items = items

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "customer_mobile": self.customer_mobile,
            "timestamp": self.timestamp,
            "items": self.items,
        }

    @staticmethod
    def load_orders():
        if os.path.exists(ORDER_FILE):
            with open(ORDER_FILE, 'r') as file:
                return json.load(file)
        return []

    @staticmethod
    def save_orders(orders):
        with open(ORDER_FILE, 'w') as file:
            json.dump(orders, file, indent=4)

class OrderManagementSystem:
    def __init__(self):
        self.menu = Menu(MENU_FILE)

    def take_order(self):
        customer_name = input("Enter customer name: ")
        customer_mobile = input("Enter customer mobile number: ")
        order_items = []

        while True:
            item_id = input("Enter item ID to order (or 'done' to finish): ")
            if item_id.lower() == 'done':
                break
            
            item_found = False
            for category, items in self.menu.items.items():
                for item in items:
                    if item['item id'] == item_id:
                        qty = int(input(f"Enter quantity for {item['item name']}: "))
                        order_items.append({
                            "item_id": item['item id'],
                            "item_name": item['item name'],
                            "quantity": qty,
                            "price": item['price']
                        })
                        item_found = True
                        break
                if item_found:
                    break
            
            if not item_found:
                print("Item ID not found. Please try again.")
        
        order = Order(customer_name, customer_mobile, order_items)
        orders = Order.load_orders()
        orders.append(order.to_dict())
        Order.save_orders(orders)

        print(f"Order placed successfully! Your order ID is:{order.order_id}")

    def update_order(self):
        order_id = input("Enter order ID: ")
        orders = Order.load_orders()

        for order in orders:
            if order['order_id'] == order_id:
                print("Current order items:")
                for i, item in enumerate(order['items']):
                    print(f"{i+1}. {item['item_name']} (ID: {item['item_id']}), Quantity: {item['quantity']}")

                while True:
                    print("\nOptions:")
                    print("1. Add new item")
                    print("2. Update existing item quantity")
                    print("3. Cancel an item")
                    print("4. Done")

                    choice = input("Choose an option: ")

                    if choice == '1':
                        new_item_id = input("Enter new item ID to add: ")
                        item_found = False
                        for category, items in self.menu.items.items():
                            for item in items:
                                if item['item id'] == new_item_id:
                                    qty = int(input(f"Enter quantity for {item['item name']}: "))
                                    order['items'].append({
                                        "item_id": item['item id'],
                                        "item_name": item['item name'],
                                        "quantity": qty,
                                        "price": item['price']
                                    })
                                    item_found = True
                                    break
                            if item_found:
                                break
                        if not item_found:
                            print("Item ID not found. Please try again.")

                    elif choice == '2':
                        item_id = input("Enter item ID to update: ")
                        for item in order['items']:
                            if item['item_id'] == item_id:
                                new_qty = int(input("Enter new quantity: "))
                                item['quantity'] = new_qty
                                break
                        else:
                            print("Item ID not found in the order.")

                    elif choice == '3':
                        item_id = input("Enter item ID to cancel: ")
                        for item in order['items']:
                            if item['item_id'] == item_id:
                                order['items'].remove(item)
                                print("Item cancelled successfully!")
                                break
                        else:
                            print("Item ID not found in the order.")

                    elif choice == '4':
                        order['timestamp'] = datetime.now().strftime('%d-%b-%Y %I:%M:%p')
                        Order.save_orders(orders)
                        print("Order updated successfully!")
                        return

                    else:
                        print("Invalid choice. Please try again.")

        print("No matching order found.")

    def cancel_order(self):
        order_id = input("Enter order ID: ")
        orders = Order.load_orders()
        
        for order in orders:
            if order['order_id'] == order_id:
                orders.remove(order)
                Order.save_orders(orders)
                print(f"Order cancelled successfully! Cancel Order ID is:{order_id}")
                return
        
        print("No matching order found.")

    def see_all_orders(self):
        orders = Order.load_orders()
        if not orders:
            print("No orders found.")
            return
        
        print("\nAll Orders:")
        for order in orders:
            print(f"\nOrder ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Mobile Number: {order['customer_mobile']}")
            print(f"Order Timestamp: {order['timestamp']}")
            print("Items:")
            for item in order['items']:
                print(f"  - {item['item_name']} (ID: {item['item_id']}), Quantity: {item['quantity']}, Price: {item['price']}")
            print("----------")

    def find_order(self):
        order_id = input("Enter order ID: ")
        orders = Order.load_orders()

        for order in orders:
            if order['order_id'] == order_id:
                print("\nOrder found:")
                print(f"Order ID: {order['order_id']}")
                print(f"Customer Name: {order['customer_name']}")
                print(f"Mobile Number: {order['customer_mobile']}")
                print(f"Order Timestamp: {order['timestamp']}")
                print("Items:")
                for item in order['items']:
                    print(f"  - {item['item_name']} (ID: {item['item_id']}), Quantity: {item['quantity']}, Price: {item['price']}")
                return
    
        print("No matching order found.")

# def run():
#     system = OrderManagementSystem()
#     while True:
#         print("\nOrder Management System")
#         print("1. Take New Order")
#         print("2. Update Order")
#         print("3. Cancel Order")
#         print("4. Display Menu")
#         print("5. See All Orders")
#         print("6. Find Order")
#         print("7. Exit")

#         choice = input("Enter your choice: ")
#         if choice == '1':
#             system.take_order()
#         elif choice == '2':
#             system.update_order()
#         elif choice == '3':
#             system.cancel_order()
#         elif choice == '4':
#             system.menu.display()
#         elif choice == '5':
#             system.see_all_orders()
#         elif choice == '6':
#             system.find_order()
#         elif choice == '7':
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     run()
