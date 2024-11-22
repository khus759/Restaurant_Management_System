from datetime import datetime
from Src.Order_management.order_data import (
    load_menu, load_orders, save_orders, generate_order_id, load_current_user
)
from Src.Utility.validation import *
from Src.Utility.user_input import get_valid_input
from Src.Messages.order import OrderOutputHandler
from Src.Utility.color import Colors
from Src.Error.log_exception import logging

class OrderManagementSystem:
    def __init__(self):
        self.menu = load_menu()
        self.orders = load_orders()
        self.output_handler = OrderOutputHandler()
        self.current_user_email = load_current_user().get('email')  # Load email of current logged-in user

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

            # Handle size selection
            if 'single' in item['prices']:
                size = 'single'
            elif 'half' in item['prices'] or 'full' in item['prices']:
                size = input("Enter size (half/full): ").lower()
                if size not in item['prices']:
                    self.output_handler.invalid_size()
                    continue
            else:
                print("Error: Invalid price configuration.")
                continue

            price = item['prices'][size]
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Error: Quantity must be a positive integer.")
                    continue
            except Exception as obj:
                logging.exception("exception Details")
                print("Error: Please enter a valid integer for quantity.")
                continue

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

        if not order_items:
            self.output_handler.no_items_in_order()
            return

        order = {
            'order_id': order_id,
            'customer_name': customer_name,
            'mobile_number': mobile_number,
            # 'user_email': self.current_user_email,
            'order_items': order_items,
            'total_order_price': total_order_price,
            'order_date': datetime.now().strftime('%d-%b-%Y %I:%M:%p'),
            'status': 'Processing',
            'user_email': self.current_user_email
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

    # def update_order(self):
    #     identifier = input("Enter order ID or mobile number to update: ")
    #     order = self.find_order_by_id_or_mobile(identifier)

    #     if not order:
    #         self.output_handler.item_not_found()
    #         return

    #     if order['status'] != 'Processing':
    #         print("Only orders with status 'Processing' can be updated.")
    #         return

    #     while True:
    #         print("\n1. Update Item Quantity")
    #         print("2. Add New Item")
    #         print("3. Remove Item")
    #         print("4. Finish Update")
    #         choice = input("Enter your choice: ")

    #         if choice == '1':
    #             item_id = input("Enter item ID to update quantity: ").upper()
    #             for item in order['order_items']:
    #                 if item['item_id'] == item_id:
    #                     new_quantity = int(input("Enter new quantity: "))
    #                     item['quantity'] = new_quantity
    #                     size = item.get('size', 'single')
    #                     price = self.find_item_by_id(item_id)['prices'].get(size, 0)
    #                     item['total_price'] = new_quantity * price
    #                     print("Item quantity updated.")
    #                     break
    #             else:
    #                 self.output_handler.item_not_found()

    #         elif choice == '2':
    #             item_id = input("Enter item ID to add: ").upper()
    #             item = self.find_item_by_id(item_id)
    #             if not item:
    #                 self.output_handler.item_not_found()
    #                 continue

    #             size = 'single' if 'single' in item['prices'] else None
    #             if 'half' in item['prices'] or 'full' in item['prices']:
    #                 size = input("Enter size (half/full): ").lower()
    #                 if size not in item['prices']:
    #                     self.output_handler.invalid_size()
    #                     continue

    #             price = item['prices'][size]
    #             quantity = int(input("Enter quantity: "))
    #             total_price = price * quantity

    #             if not self.check_stock(item, quantity):
    #                 self.output_handler.insufficient_stock()
    #                 continue

    #             order['order_items'].append({
    #                 'item_id': item_id,
    #                 'item_name': item['item name'],
    #                 'size': size,
    #                 'quantity': quantity,
    #                 'total_price': total_price
    #             })
    #             print("New item added to order.")

    #         elif choice == '3':
    #             item_id = input("Enter item ID to remove: ").upper()
    #             for item in order['order_items']:
    #                 if item['item_id'] == item_id:
    #                     order['order_items'].remove(item)
    #                     print("Item removed from order.")
    #                     break
    #             else:
    #                 self.output_handler.item_not_found()

    #         elif choice == '4':
    #             order['total_order_price'] = sum(item['total_price'] for item in order['order_items'])
    #             break

    #         else:
    #             print("Invalid choice. Please try again.")

    #     save_orders(self.orders)
    #     print("Order updated successfully.")

    def update_order(self):
        identifier = input("Enter order ID or mobile number to update: ").strip()
        try:
            order = self.find_order_by_id_or_mobile(identifier)
        except Exception as e:
            logging.exception("exception details")
            print(f"Error while fetching the order: {e}")
            return

        if not order:
            self.output_handler.item_not_found()
            return

        if order.get('status') != 'Processing':
            print("Only orders with status 'Processing' can be updated.")
            return

        while True:
            print("\n1. Update Item Quantity")
            print("2. Add New Item")
            print("3. Remove Item")
            print("4. Finish Update")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                try:
                    item_id = input("Enter item ID to update quantity: ").upper()
                    for item in order['order_items']:
                        if item['item_id'] == item_id:
                            new_quantity = int(input("Enter new quantity: "))
                            if new_quantity <= 0:
                                print("Quantity must be greater than zero.")
                                continue

                            size = item.get('size', 'single')
                            price = self.find_item_by_id(item_id)['prices'].get(size, 0)
                            item['quantity'] = new_quantity
                            item['total_price'] = new_quantity * price
                            print("Item quantity updated.")
                            break
                    else:
                        self.output_handler.item_not_found()
                except ValueError:
                    logging.exception("exception details")
                    print("Invalid input. Quantity must be a number.")
                except Exception as e:
                    logging.exception("exception details")
                    print(f"An error occurred: {e}")

            elif choice == '2':
                try:
                    item_id = input("Enter item ID to add: ").upper()
                    item = self.find_item_by_id(item_id)
                    if not item:
                        self.output_handler.item_not_found()
                        continue

                    size = 'single' if 'single' in item['prices'] else None
                    if 'half' in item['prices'] or 'full' in item['prices']:
                        size = input("Enter size (half/full): ").lower()
                        if size not in item['prices']:
                            self.output_handler.invalid_size()
                            continue

                    price = item['prices'][size]
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than zero.")
                        continue

                    if not self.check_stock(item, quantity):
                        self.output_handler.insufficient_stock()
                        continue

                    order['order_items'].append({
                        'item_id': item_id,
                        'item_name': item['item name'],
                        'size': size,
                        'quantity': quantity,
                        'total_price': price * quantity
                    })
                    print("New item added to order.")
                except ValueError:
                    logging.exception("exception details")
                    print("Invalid input. Quantity must be a number.")
                except Exception as e:
                    logging.exception("exception details")
                    print(f"An error occurred: {e}")

            elif choice == '3':
                try:
                    item_id = input("Enter item ID to remove: ").upper()
                    for item in order['order_items']:
                        if item['item_id'] == item_id:
                            order['order_items'].remove(item)
                            print("Item removed from order.")
                            break
                    else:
                        self.output_handler.item_not_found()
                except Exception as e:
                    logging.exception("exception details")
                    print(f"An error occurred: {e}")

            elif choice == '4':
                try:
                    order['total_order_price'] = sum(item['total_price'] for item in order['order_items'])
                    print("Order updated successfully.")
                    save_orders(self.orders)
                    break
                except Exception as e:
                    logging.exception("exception details")
                    print(f"An error occurred while saving the order: {e}")
                    return

            else:
                print("Invalid choice. Please try again.")


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
            print(f"{Colors.LIGHT_AQUA}\nCategory: {category}{Colors.RESET}")
            print(f"{Colors.LIGHT_TEAL}ITEM ID\t ITEM NAME\t\t\t PRICE\t\t\t\t\tINGREDIENTS{Colors.RESET}")
            print(f"{Colors.LIGHT_PINK}-{Colors.RESET}"*120)
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
