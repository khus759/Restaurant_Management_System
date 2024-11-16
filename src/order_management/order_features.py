from datetime import datetime
from Src.Order_management.order_data import load_menu, load_orders, save_orders, generate_order_id
from Src.Utility.validation import *
from Src.Utility.user_input import get_valid_input
from Src.Messages.order import OrderOutputHandler  

class OrderManagementSystem:
    def __init__(self):
        self.menu = load_menu()
        self.orders = load_orders()
        self.output_handler = OrderOutputHandler()  

    def take_order(self):
        customer_name = get_valid_input("Enter customer name: ", validate_name)
        mobile_number = get_valid_input("Enter mobile number: ", validate_phone_number)
        order_id = generate_order_id()

        order_items = []
        total_order_price = 0

        while True:
            item_id = input("Enter item ID (or 'done' to finish): ").upper()
            if item_id == 'DONE':
                break

            item = self.find_item_by_id(item_id)
            if not item:
                self.output_handler.item_not_found()
                continue

            size = 'single'
            if 'half' in item['prices'] or 'full' in item['prices']:
                size = input("Enter size (half/full): ").lower()
                if size not in item['prices']:
                    self.output_handler.invalid_size()
                    continue
                price = item['prices'][size]
            else:
                price = item['prices']['single']

            quantity = int(input("Enter quantity: "))
            total_price = price * quantity

            if not self.check_stock(item, quantity):
                self.output_handler.insufficient_stock()
                continue

            order_items.append({
                'item_id': item_id,
                'item_name': item['item name'],
                'size': size,
                'quantity': quantity,
                'total_price': total_price
            })
            total_order_price += total_price

        # Check if order_items is empty before proceeding
        if not order_items:
            self.output_handler.no_items_in_order()
            return

        # Create order if items are added
        order = {
            'order_id': order_id,
            'customer_name': customer_name,
            'mobile_number': mobile_number,
            'order_items': order_items,
            'total_order_price': total_order_price,
            'order_date': datetime.now().strftime('%d-%b-%Y %I:%M:%p'),
            'status': 'Processing'
        }

        self.orders.append(order)
        save_orders(self.orders)
        self.output_handler.show_order_placed(order_id, total_order_price)

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

    def check_order(self):
        identifier = input("Enter order ID or mobile number to check: ")
        order = self.find_order_by_id_or_mobile(identifier)
        if not order:
            self.output_handler.item_not_found()
            return

        self.output_handler.show_order_details(order)

    def show_all_orders(self):
        if not self.orders:
            self.output_handler.item_not_found()
            return

        for order in self.orders:
            self.output_handler.show_order_details(order)

    def update_order(self):
        identifier = input("Enter order ID or mobile number to update: ")
        order = self.find_order_by_id_or_mobile(identifier)

        if not order:
            self.output_handler.item_not_found()
            return

        if order['status'] != 'Processing':
            print("Only orders with status 'Processing' can be updated.")
            return

        while True:
            print("\n1. Update Item Quantity")
            print("2. Add New Item")
            print("3. Remove Item")
            print("4. Finish Update")
            choice = input("Enter your choice: ")

            if choice == '1':
                item_id = input("Enter item ID to update quantity: ").upper()
                for item in order['order_items']:
                    if item['item_id'] == item_id:
                        new_quantity = int(input("Enter new quantity: "))
                        item['quantity'] = new_quantity
                        if 'half' in self.find_item_by_id(item_id)['prices'] or 'full' in self.find_item_by_id(item_id)['prices']:
                            size = item.get('size')
                            price = self.find_item_by_id(item_id)['prices'][size]
                        else:
                            price = self.find_item_by_id(item_id)['prices']['single']
                        item['total_price'] = new_quantity * price
                        print("Item quantity updated.")
                        break
                else:
                    self.output_handler.item_not_found()

            elif choice == '2':
                item_id = input("Enter item ID to add: ").upper()
                item = self.find_item_by_id(item_id)
                if not item:
                    self.output_handler.item_not_found()
                    continue

                size = 'single'
                if 'half' in item['prices'] or 'full' in item['prices']:
                    size = input("Enter size (half/full): ").lower()
                    if size not in item['prices']:
                        self.output_handler.invalid_size()
                        continue
                    price = item['prices'][size]
                else:
                    price = item['prices']['single']

                quantity = int(input("Enter quantity: "))
                total_price = price * quantity

                if not self.check_stock(item, quantity):
                    self.output_handler.insufficient_stock()
                    continue

                order['order_items'].append({
                    'item_id': item_id,
                    'item_name': item['item name'],
                    'size': size,
                    'quantity': quantity,
                    'total_price': total_price
                })
                print("New item added to order.")

            elif choice == '3':
                item_id = input("Enter item ID to remove: ").upper()
                for item in order['order_items']:
                    if item['item_id'] == item_id:
                        order['order_items'].remove(item)
                        print("Item removed from order.")
                        break
                else:
                    self.output_handler.item_not_found()

            elif choice == '4':
                order['total_order_price'] = sum(item['total_price'] for item in order['order_items'])
                break

            else:
                print("Invalid choice. Please try again.")

        save_orders(self.orders)
        print("Order updated successfully.")

    def cancel_order(self):
        identifier = input("Enter order ID or mobile number to cancel: ")
        order = self.find_order_by_id_or_mobile(identifier)
        if not order:
            self.output_handler.item_not_found()
            return

        self.orders.remove(order)
        save_orders(self.orders)
        print("Order cancelled successfully.")

    def find_order_by_id_or_mobile(self, identifier):
        for order in self.orders:
            if order['order_id'] == identifier or order['mobile_number'] == identifier:
                return order
        return None

    def show_menu(self):
        for category, items in self.menu.items():
            print(f"\nCategory: {category}")
            for item in items:
                item_id = item['item id']
                item_name = item['item name']
                prices = item['prices']
                price_details = ', '.join([f"{size}: {price}" for size, price in prices.items()])
                ingredients = item.get('ingredients', 'No ingredients listed')
                if isinstance(ingredients, list):
                    ingredients = ', '.join(ingredients)
                self.output_handler.show_menu_item(item_id, item_name, price_details, ingredients)

    def exit_system(self):
        self.output_handler.exit_message()
    
    def welcome_system(self):
        self.output_handler.welcome_message()