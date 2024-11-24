from Src.Utility.color import Colors
class OrderOutputHandler:
    def __init__(self):
        self.color = Colors()

    def show_order_placed(self, order_id, total_order_price):
        print(f"{Colors.GREEN}✔️ Order placed successfully with ID: {order_id} and Total Price: ₹{total_order_price} Only {Colors.RESET}")

    def item_not_found(self):
        print(f"{Colors.RED}❌ Item not found.{Colors.RESET}")

    def invalid_size(self):
        print(f"{Colors.RED}❌ Invalid size. Please select a valid option.{Colors.RESET}")

    def insufficient_stock(self):
        print(f"{Colors.RED}❌ Insufficient stock available for this item.{Colors.RESET}")

    def show_order_details(self, order):
        print(f"\n{Colors.LIGHT_VIOLET}Order Details{Colors.RESET}")
        print(f"{Colors.LIGHT_BEIGE}={Colors.RESET}" * 50)
        print(f"Order ID      : {order['order_id']}")
        print(f"Customer Name : {order['customer_name']}")
        print(f"Mobile Number : {order['mobile_number']}")
        print(f"Order Date    : {order['order_date']}")
        print(f"Status        : {order['status']}")
        print("Order Items:")
        print(f"{Colors.LIGHT_ORANGE}-{Colors.RESET}" * 50)
        for item in order['order_items']:
            print(f"  - {item['item_name']} (ID: {item['item_id']}, Size: {item['size']})")
            print(f"    Quantity: {item['quantity']}")
            print(f"    Total Price: ₹{item['total_price']}")
            print("-" * 50)
        print(f"{Colors.LIGHT_BEIGE}={Colors.RESET}" * 50)

    def show_menu_item(self, item_id, item_name, price_details, ingredients):
        print(f"{Colors.LIGHT_CORAL}{item_id:<10}{Colors.RESET}{Colors.LIGHT_TEAL}{item_name:<30}{Colors.RESET}{Colors.LIGHT_PINK}{price_details:<40}{Colors.RESET}{Colors.LIGHT_ORANGE}{ingredients:<50}{Colors.RESET}")
        print(f"{Colors.LIGHT_VIOLET}*{Colors.RESET}"*120) 

    def order_update_success(self, order_id):
        print(f"{Colors.GREEN}✔️ Order with ID {order_id} has been successfully updated.{Colors.RESET}")

    def order_cancel_success(self, order_id):
        print(f"{Colors.GREEN}✔️ Order with ID {order_id} has been successfully canceled.{Colors.RESET}")

    def order_not_found(self, order_id):
        print(f"{Colors.RED}❌ No order found with ID {order_id}.{Colors.RESET}")

    def order_status(self, order_id, status):
        print(f"{Colors.BLUE}Order ID: {order_id} - Current Status: {status}{Colors.RESET}")

    def invalid_input(self, field):
        print(f"{Colors.RED}❌ Invalid input for {field}. Please try again.{Colors.RESET}")

    def order_save_error(self, exception):
        print(f"{Colors.RED}❌ An error occurred while saving the order: {exception}{Colors.RESET}")

    def no_orders_found(self):
        print(f"{Colors.RED}❌ No orders found.{Colors.RESET}")

    def display_inventory(self, inventory):
        print(f"\n{Colors.BLUE}Inventory Details{Colors.RESET}")
        print(f"{Colors.YELLOW}={Colors.RED}" * 50)
        for item in inventory:
            print(f"Item ID: {item['id']} - Name: {item['name']}, Stock: {item['stock']} {item['unit']}")
        print(f"{Colors.YELLOW}={Colors.RESET}" * 50)

    def inventory_update_success(self, item_name):
        print(f"{Colors.GREEN}✔️ Inventory updated successfully for {item_name}.{Colors.RESET}")

    def invalid_quantity(self):
        print(f"{Colors.RED}❌ Invalid quantity entered. Please enter a valid number.{Colors.RESET}")

    def welcome_message(self):
        print(f"{Colors.LIGHT_PEACH}  Welcome to the Order Management System! Please follow the prompts to continue.{Colors.RESET}")

    def exit_message(self):
        print(f"{Colors.LIGHT_TURQUOISE}  Thank you for using the Order Management System. Goodbye!{Colors.RESET}")

    def generate_message(self, e):
        print(f"{Colors.RED}❌ Error generating order ID: {e}{Colors.RESET}")
    
    def no_items_in_order(self):
        print(f"{Colors.RED} ❌ No items were added to the order. Order cannot be placed.{Colors.RESET}")

    
    