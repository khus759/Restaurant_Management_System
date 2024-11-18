import json
from datetime import datetime
from collections import Counter
from Src.Utility.path_manager import order_file
from Src.Messages.reports import Report

class OrderReport:
    def __init__(self, order_file=order_file):
        self.order_file = order_file
        self.orders = self.load_orders()
        self.report = Report()

    def load_orders(self):
        # Load the orders from the JSON file
        with open(self.order_file, 'r') as file:
            return json.load(file)

    def show_ordered_items_summary(self):
        # Ask user for date input
        date_input = input("Enter date (YYYY, YYYY-MM, or YYYY-MM-DD): ").strip()

        item_counter = Counter()  # To count ordered items
        order_details = {}  # To store details about each ordered item (e.g., quantity, order time, employee)

        for order in self.orders:
            order_date = datetime.strptime(order["order_date"], "%d-%b-%Y %I:%M:%p")
            formatted_date = order_date.strftime('%Y-%m-%d')
            formatted_month = order_date.strftime('%Y-%m')
            formatted_year = order_date.strftime('%Y')

            # Check if the order date matches the input
            if (len(date_input) == 10 and formatted_date == date_input) or \
               (len(date_input) == 7 and formatted_month == date_input) or \
               (len(date_input) == 4 and formatted_year == date_input):

                # Fetch employee name and email directly from the order, defaulting to "Unknown" if missing
                employee_name = order.get("customer_name", "Unknown")
                employee_email = order.get("user_email", "Unknown")

                for item in order["order_items"]:
                    item_key = (item["item_id"], item["item_name"])  # Tuple key for item ID and name
                    item_counter[item_key] += item["quantity"]

                    # Store the order details (e.g., quantity, order date, employee name/email)
                    if item_key not in order_details:
                        order_details[item_key] = []

                    order_details[item_key].append({
                        "quantity": item["quantity"],
                        "order_date": formatted_date,
                        "order_time": order_date.strftime('%I:%M %p'),
                        "employee_name": employee_name,
                        "employee_email": employee_email
                    })

        if item_counter:
            # Show order summary and most/least ordered items
            self.report.show_order_summary_header(date_input)
            for (item_id, item_name), total_quantity in item_counter.most_common():
                self.report.show_item_summary(item_id, item_name, total_quantity)
                for detail in order_details[(item_id, item_name)]:
                    self.report.show_order_details(detail)
        else:
            self.report.no_orders_found(date_input)
