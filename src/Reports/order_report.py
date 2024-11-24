import json
from datetime import datetime,timedelta
from collections import Counter
from Src.Utility.path_manager import order_file
from Src.Messages.reports import Report
from Src.Error.log_exception import logging


class OrderReport:
    def _init_(self, order_file=order_file):
        self.order_file = order_file
        self.orders = self.load_orders()
        self.report = Report()

    def load_orders(self):
        # Load the orders from the JSON file
        with open(self.order_file, 'r') as file:
            return json.load(file)

    def show_ordered_items_summary(self):
        # Ask user for date input
        date_input = input(
            "Enter a date (YYYY, YYYY-MM, or YYYY-MM-DD) or date range (YYYY-MM-DD to YYYY-MM-DD): "
        ).strip()

        item_counter = Counter()  # To count ordered items
        order_details = {}  # To store details about each ordered item (e.g., quantity, order time, employee)

        # Parse date range input
        if "to" in date_input:
            try:
                start_date_str, end_date_str = [date.strip() for date in date_input.split("to")]
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            except ValueError:

                logging.exception("exception details")

                print("Invalid date range format. Use YYYY-MM-DD to YYYY-MM-DD.")
                return
        else:
            # Handle single date input
            start_date = end_date = None
            if len(date_input) == 10:
                start_date = end_date = datetime.strptime(date_input, "%Y-%m-%d")
            elif len(date_input) == 7:
                start_date = datetime.strptime(date_input, "%Y-%m-01")
                end_date = datetime.strptime(date_input, "%Y-%m-01").replace(day=28) + timedelta(days=4)
                end_date = end_date.replace(day=1) - timedelta(days=1)  # Last day of the month
            elif len(date_input) == 4:
                start_date = datetime.strptime(date_input, "%Y-01-01")
                end_date = datetime.strptime(date_input, "%Y-12-31")
            else:
                print("Invalid date format. Use YYYY, YYYY-MM, or YYYY-MM-DD.")
                return

        for order in self.orders:
            order_date = datetime.strptime(order["order_date"], "%d-%b-%Y %I:%M:%p")

            # Check if the order date is within the input date range
            if start_date <= order_date <= end_date:
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
                        "order_date": order_date.strftime('%Y-%m-%d'),
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

            self.report.no_orders_found(date_input)

