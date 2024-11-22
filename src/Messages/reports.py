from Src.Utility.color import Colors
class Report:
    def __init__(self):
        self.colors = Colors()

    def show_reservations_header(self,date_input):
      print(f"\nReservations on {date_input}:")

    def show_reservation_details(self,reservation):
        print(
            f"Name: {reservation['name']}, "
            f"Phone: {reservation['phone']}, "
            f"Booking Date: {reservation['booking_date']}, "
            f"Time: {reservation['time']}, "
            f"Table: {reservation['table_id']}, "
            f"Status: {reservation['status']}"
        )

    def no_reservations_found(self,date_input):
        print(f"❌ No reservations found for {date_input}.")

    def show_canceled_reservations_header(self):
        print("\nCanceled Reservations:")

    def show_canceled_reservation_details(self,reservation):
        print(
            f"Name: {reservation['name']}, "
            f"Phone: {reservation['phone']}, "
            f"Cancellation Date: {reservation['cancellation_date']}, "
            f"Time: {reservation['time']}, "
            f"Table: {reservation['table_id']}"
        )

    def no_canceled_reservations_found(self):
        print("❌ No canceled reservations found for the specified date or month.")
    
    def show_order_summary_header(self,date_input):
        print(f"\nItem Order Summary for {date_input}:")

    def show_item_summary(self,item_id, item_name, total_quantity):
        print(f"\nItem ID: {item_id}, Item Name: {item_name}, Total Quantity Ordered: {total_quantity}")

    def show_order_details(self,detail):
        print(
            f"  - Quantity: {detail['quantity']}, "
            f"Date: {detail['order_date']}, "
            f"Time: {detail['order_time']}, "
            f"Taken by: {detail['employee_name']}"
        )

    def no_orders_found(self,date_input):
        print(f"❌ No orders found for the specified date: {date_input}")
    
    
    def show_expiring_ingredients_header(self,days_until_expiration):
        print(f"Ingredients Nearing Expiration in the Next {days_until_expiration} Days:")

    def show_expiring_ingredient_entry(self,entry):
        print(f"Category: {entry['category']}, Item: {entry['item_name']}, "
            f"Ingredient: {entry['ingredient']}, Expiration Date: {entry['expiration_date']}")

    def no_expiring_ingredients(self,days_until_expiration):
        print(f"No ingredients nearing expiration in the next {days_until_expiration} days.")

    def show_low_stock_header(self,low_stock_threshold):
        print(f"\nIngredients Soon Going Out of Stock (below {low_stock_threshold} units):")

    def show_low_stock_entry(self,entry):
        print(f"Category: {entry['category']}, Item: {entry['item_name']}, "
            f"Ingredient: {entry['ingredient']}, Quantity: {entry['quantity']}")

    def no_low_stock_ingredients(self,low_stock_threshold):
        print(f"No ingredients are low in stock (below {low_stock_threshold} units).")

    def show_summary_header(self):
        print("\nSummary of Ingredients Nearing Expiration and Low Stock:")

    def show_summary_category(self,category):
        print(f"\nCategory: {category}")

    def show_summary_item(self,item_name, ingredients):
        ingredients_list = ', '.join(ingredients)
        print(f"  Item: {item_name}, Ingredients: {ingredients_list}")

    def no_summary(self):
        print("No ingredients nearing expiration or low in stock to display in the summary.")
    
    def welcome_message(self):
        print(f"{Colors.LIGHT_PINK}  Welcome to the Reports Management ! Please follow the prompts to continue.{Colors.RESET}")

    def exit_message(self):
        print(f"{Colors.LIGHT_PEACH}  Thank you for using the Reports Management. Goodbye!{Colors.RESET}")
    
    def show_order_summary_header(self, date_input):
       print(f"{Colors.LIGHT_ORANGE}Order Summary for Date: {date_input}{Colors.RESET}")

    def show_item_summary(self, item_id, item_name, total_quantity):
       print(f"\n{Colors.LIGHT_PINK}Item ID: {item_id}, Item Name: {item_name}, Total Quantity Ordered: {total_quantity}{Colors.RESET}")

    def show_order_details(self, detail):
       print(f"{Colors.LIGHT_PEACH}  - Quantity: {detail['quantity']}, Date: {detail['order_date']}, {Colors.RESET}"
             f"\n{Colors.LIGHT_CORAL}Time: {detail['order_time']}, Taken by: {detail['employee_name']}, Staff email: ({detail['employee_email']}){Colors.RESET}")

    def no_orders_found(self, date_input):
       print(f"{Colors.CORAL}No orders found for the date: {date_input}{Colors.RESET}")





    


