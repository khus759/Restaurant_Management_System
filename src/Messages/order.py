class OrderOutputHandler():
    def show_order_placed(self, order_id, total_order_price):
        print(f"Order placed successfully with ID: {order_id} and Total Price: {total_order_price}")

    def item_not_found(self):
        print("Item not found.")

    def invalid_size(self):
        print("Invalid size. Please select a valid option.")

    def insufficient_stock(self):
        print("Insufficient stock available for this item.")

    def show_order_details(self, order):
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
            print(f"  - {item['item_name']} (ID: {item['item_id']}, Size: {item['size']})")
            print(f"    Quantity: {item['quantity']}")
            print(f"    Total Price: {item['total_price']}")
            print("-" * 50)
        print("=" * 50)

    def show_menu_item(self, item_id, item_name, price_details, ingredients):
        print(f"{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}")

    def order_update_success(self, order_id):
        print(f"Order with ID {order_id} has been successfully updated.")

    def order_cancel_success(self, order_id):
        print(f"Order with ID {order_id} has been successfully canceled.")

    def order_not_found(self, order_id):
        print(f"No order found with ID {order_id}.")

    def order_status(self, order_id, status):
        print(f"Order ID: {order_id} - Current Status: {status}")

    def invalid_input(self, field):
        print(f"Invalid input for {field}. Please try again.")

    def order_save_error(self, exception):
        print(f"An error occurred while saving the order: {exception}")

    def no_orders_found(self):
        print("No orders found.")

    def display_inventory(self, inventory):
        print("\nInventory Details")
        print("=" * 50)
        for item in inventory:
            print(f"Item ID: {item['id']} - Name: {item['name']}, Stock: {item['stock']} {item['unit']}")
        print("=" * 50)

    def inventory_update_success(self, item_name):
        print(f"Inventory updated successfully for {item_name}.")

    def invalid_quantity(self):
        print("Invalid quantity entered. Please enter a valid number.")

    def welcome_message(self):
        print("Welcome to the Order Management System! Please follow the prompts to continue.")

    def exit_message(self):
        print("Thank you for using the Order Management System. Goodbye!")

    def generate_message(self,e):
        print("Error generating order ID:",e)
