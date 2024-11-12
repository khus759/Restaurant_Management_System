import json
from datetime import datetime
from collections import Counter
from Src.Utility.path_manager import order_file

class OrderReport:
    def __init__(self, order_file=order_file):
        self.order_file = order_file
        self.orders = self.load_orders()

    def load_orders(self):
        with open(self.order_file, 'r') as file:
            return json.load(file)

    def show_ordered_items_summary(self):
        # Taking user input for date filter (year, month, or day)
        date_input = input("Enter date (YYYY, YYYY-MM, or YYYY-MM-DD): ").strip()

        # Define counters for item frequencies
        item_counter = Counter()

        # Parse orders and accumulate item quantities
        for order in self.orders:
            # Parse the order date
            order_date = datetime.strptime(order["order_date"], "%d-%b-%Y %I:%M:%p")
            formatted_date = order_date.strftime('%Y-%m-%d')
            formatted_month = order_date.strftime('%Y-%m')
            formatted_year = order_date.strftime('%Y')

            # Check if order matches the specified date filter
            if (len(date_input) == 10 and formatted_date == date_input) or \
               (len(date_input) == 7 and formatted_month == date_input) or \
               (len(date_input) == 4 and formatted_year == date_input):
                for item in order["order_items"]:
                    item_counter[(item["item_id"], item["item_name"])] += item["quantity"]

        # Display ordered items summary
        if item_counter:
            print(f"\nItem Order Summary for {date_input}:")
            # Sort items by quantity ordered (most to least)
            for (item_id, item_name), quantity in item_counter.most_common():
                print(f"Item ID: {item_id}, Item Name: {item_name}, Total Quantity Ordered: {quantity}")
        else:
            print(f"No orders found for the specified date: {date_input}")

