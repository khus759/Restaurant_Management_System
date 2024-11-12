from datetime import datetime
from Src.Order_management.order_data import load_menu, load_orders, save_orders, generate_order_id
from Src.Utility.validation import *
from Src.Utility.user_input import get_valid_input


class OrderManagementSystem:
    def __init__(self):
        self.menu = load_menu()
        self.orders = load_orders()

    def take_order(self):
        customer_name = get_valid_input("Enter customer name: ",validate_name)
        mobile_number = get_valid_input("Enter mobile number: ",validate_phone_number)
        order_id = generate_order_id()

        order_items = []
        while True:
            item_id = input("Enter item ID (or 'done' to finish): ")
            if item_id.lower() == 'done':
                break

            item = self.find_item_by_id(item_id)
            if not item:
                print("Item not found.")
                continue

            if 'half' in item['prices'] or 'full' in item['prices']:
                size = input("Enter size (half/full): ").lower()
                if size not in item['prices']:
                    print("Invalid size.")
                    continue
                price = item['prices'][size]
            else:
                price = item['prices']['Price']

            quantity = int(input("Enter quantity: "))
            total_price = price * quantity

            if not self.check_stock(item, quantity):
                print("Insufficient stock.")
                continue

            order_items.append({
                'item_id': item_id,
                'item_name': item['item name'],
                'quantity': quantity,
                'total_price': total_price
            })

        order = {
            'order_id': order_id,
            'customer_name': customer_name,
            'mobile_number': mobile_number,
            'order_items': order_items,
            'order_date': datetime.now().strftime('%d-%b-%Y %I:%M:%p'),
            'status': 'Processing'
        }

        self.orders.append(order)
        save_orders(self.orders)
        print(f"Order placed successfully with ID: {order_id}")

    def find_item_by_id(self, item_id):
        for category, items in self.menu.items():
            for item in items:
                if item['item id'] == item_id:
                    return item
        return None

    def check_stock(self, item, quantity):
        if 'stock_ingredients' not in item:
            return True
        for ingredient, expiry in item['stock_ingredients'].items():
            if datetime.strptime(expiry, '%Y-%m-%d') < datetime.now():
                return False
        return True

    def update_order(self):
        identifier = input("Enter order ID or mobile number to update: ")
        order = self.find_order_by_id_or_mobile(identifier)
        if not order:
            print("Order not found.")
            return
    
        while True:
            print("\n1. Update Item Quantity")
            print("2. Add New Item")
            print("3. Remove Item")
            print("4. Update Status")
            print("5. Finish Update")
            choice = input("Enter your choice: ")
    
            if choice == '1':
                item_id = get_valid_input("Enter item ID to update quantity: ",validate_item_id).upper()
                for item in order['order_items']:
                    if item['item_id'] == item_id:
                        new_quantity = int(input("Enter new quantity: "))
                        item['quantity'] = new_quantity
                        item['total_price'] = new_quantity * self.find_item_by_id(item_id)['prices']['pieces']
                        print("Item quantity updated.")
                        break
                else:
                    print("Item not found in order.")
    
            elif choice == '2':
                item_id = get_valid_input("Enter new item ID to add: ",validate_item_id)
                item = self.find_item_by_id(item_id)
                if not item:
                    print("Item not found.")
                    continue
                
                if 'half' in item['prices'] or 'full' in item['prices']:
                    size = input("Enter size (half/full): ").lower()
                    if size not in item['prices']:
                        print("Invalid size.")
                        continue
                    price = item['prices'][size]
                else:
                    price = item['prices']['pieces']
    
                quantity = int(input("Enter quantity: "))
                total_price = price * quantity
    
                if not self.check_stock(item, quantity):
                    print("Insufficient stock.")
                    continue
                
                order['order_items'].append({
                    'item_id': item_id,
                    'item_name': item['item name'],
                    'quantity': quantity,
                    'total_price': total_price
                })
                print("New item added to order.")
    
            elif choice == '3':
                item_id = get_valid_input("Enter item ID to remove: ",validate_item_id)
                for item in order['order_items']:
                    if item['item_id'] == item_id:
                        order['order_items'].remove(item)
                        print("Item removed from order.")
                        break
                else:
                    print("Item not found in order.")
    
            elif choice == '4':
                new_status = input("Enter new status (e.g., Processing, Completed, Cancelled): ")
                order['status'] = new_status
                print("Order status updated.")
    
            elif choice == '5':
                break
            
            else:
                print("Invalid choice. Please try again.")
    
        self.save_orders()
        print("Order updated successfully.")

    def cancel_order(self):
        identifier = input("Enter order ID or mobile number to cancel: ")
        order = self.find_order_by_id_or_mobile(identifier)
        if not order:
            print("Order not found.")
            return

        self.orders.remove(order)
        self.save_orders()
        print("Order cancelled successfully.")

    def find_order_by_id_or_mobile(self, identifier):
        for order in self.orders:
            if order['order_id'] == identifier or order['mobile_number'] == identifier:
                return order
        return None

    def check_order(self):
        identifier = input("Enter order ID or mobile number to check: ")
        order = self.find_order_by_id_or_mobile(identifier)
        if not order:
            print("Order not found.")
            return

        print("\nOrder Details")
        print("=" * 50)
        print(f"Order ID      : {order['order_id']}")
        print(f"Customer Name : {order['customer_name']}")
        print(f"Mobile Number : {order['mobile_number']}")
        print(f"Order Date    : {order['order_date']}")
        print(f"Status        : {order['status']}")
        print("Order Items:")
        print("-" * 50)
        for item in order['order_items']:
            print(f"  - {item['item_name']} (ID: {item['item_id']})")
            print(f"    Quantity: {item['quantity']}")
            print(f"    Total Price: {item['total_price']}")
            print("-" * 50)
        print("=" * 50)
        print("")

    def show_all_orders(self):
        if not self.orders:
            print("No orders found.")
            return

        for order in self.orders:
            status = order.get('status', 'Unknown')
            print("\nOrder Details")
            print("=" * 60)
            print(f"{'Order ID':<15}: {order['order_id']}")
            print(f"{'Customer Name':<15}: {order['customer_name']}")
            print(f"{'Mobile Number':<15}: {order['mobile_number']}")
            print(f"{'Order Date':<15}: {order['order_date']}")
            print(f"{'Status':<15}: {status}")
            print("\nOrder Items:")
            print("-" * 60)
            for item in order['order_items']:
                print(f"  - {item['item_name']} (ID: {item['item_id']})")
                print(f"    {'Quantity':<10}: {item['quantity']}")
                print(f"    {'Total Price':<10}: {item['total_price']}")
                print("-" * 60)
            print("=" * 60)
            print("")

    def show_menu(self):
        print("\nMenu:")
        header = f"{'ID':<10}{'Name':<30}{'Prices':<40}{'Ingredients':<50}"
        print(header)
        print("=" * 130)
        for category, items in self.menu.items():
            print(f"\nCategory: {category}")
            print("-" * 130)
            for item in items:
                item_id = item['item id']
                item_name = item['item name']
                prices = item['prices']
                price_details = ', '.join([f"{size}: {price}" for size, price in prices.items()])
                ingredients = item.get('ingredients', 'No ingredients listed')
                if isinstance(ingredients, list):
                    ingredients = ', '.join(ingredients)
                print(f"{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}")
            print("=" * 130)