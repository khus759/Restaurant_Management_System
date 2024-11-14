class OrderOutputHandler:
    # Define color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"

    def show_order_placed(self, order_id, total_order_price):
        print(f"{self.GREEN}✔️ Order placed successfully with ID: {order_id} and Total Price: ₹{total_order_price}{self.RESET}")

    def item_not_found(self):
        print(f"{self.RED}❌ Item not found.{self.RESET}")

    def invalid_size(self):
        print(f"{self.RED}❌ Invalid size. Please select a valid option.{self.RESET}")

    def insufficient_stock(self):
        print(f"{self.RED}❌ Insufficient stock available for this item.{self.RESET}")

    def show_order_details(self, order):
        print(f"\n{self.BLUE}Order Details{self.RESET}")
        print("=" * 50)
        print(f"Order ID      : {order['order_id']}")
        print(f"Customer Name : {order['customer_name']}")
        print(f"Mobile Number : {order['mobile_number']}")
        print(f"Order Date    : {order['order_date']}")
        print(f"Status        : {order['status']}")
        print("Order Items:")
        print("-" * 50)
        for item in order['order_items']:
            print(f"  - {item['item_name']} (ID: {item['item_id']}, Size: {item['size']})")
            print(f"    Quantity: {item['quantity']}")
            print(f"    Total Price: ₹{item['total_price']}")
            print("-" * 50)
        print("=" * 50)

    def show_menu_item(self, item_id, item_name, price_details, ingredients):
        print(f"{self.BRIGHT_MAGENTA}{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}{self.RESET}")

    def order_update_success(self, order_id):
        print(f"{self.GREEN}✔️ Order with ID {order_id} has been successfully updated.{self.RESET}")

    def order_cancel_success(self, order_id):
        print(f"{self.GREEN}✔️ Order with ID {order_id} has been successfully canceled.{self.RESET}")

    def order_not_found(self, order_id):
        print(f"{self.RED}❌ No order found with ID {order_id}.{self.RESET}")

    def order_status(self, order_id, status):
        print(f"{self.BLUE}Order ID: {order_id} - Current Status: {status}{self.RESET}")

    def invalid_input(self, field):
        print(f"{self.RED}❌ Invalid input for {field}. Please try again.{self.RESET}")

    def order_save_error(self, exception):
        print(f"{self.RED}❌ An error occurred while saving the order: {exception}{self.RESET}")

    def no_orders_found(self):
        print(f"{self.RED}❌ No orders found.{self.RESET}")

    def display_inventory(self, inventory):
        print(f"\n{self.BLUE}Inventory Details{self.RESET}")
        print("=" * 50)
        for item in inventory:
            print(f"Item ID: {item['id']} - Name: {item['name']}, Stock: {item['stock']} {item['unit']}")
        print("=" * 50)

    def inventory_update_success(self, item_name):
        print(f"{self.GREEN}✔️ Inventory updated successfully for {item_name}.{self.RESET}")

    def invalid_quantity(self):
        print(f"{self.RED}❌ Invalid quantity entered. Please enter a valid number.{self.RESET}")

    def welcome_message(self):
        print(f"{self.BLUE}Welcome to the Order Management System! Please follow the prompts to continue.{self.RESET}")

    def exit_message(self):
        print(f"{self.BLUE}Thank you for using the Order Management System. Goodbye!{self.RESET}")

    def generate_message(self, e):
        print(f"{self.RED}❌ Error generating order ID: {e}{self.RESET}")
