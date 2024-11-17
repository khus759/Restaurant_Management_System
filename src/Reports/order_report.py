import json
from datetime import datetime
from collections import Counter
from Src.Utility.path_manager import order_file, users_file
from Src.Messages.reports import Report

class OrderReport:
    def __init__(self, order_file=order_file, users_file=users_file):
        self.order_file = order_file
        self.users_file = users_file
        self.orders = self.load_orders()
        self.users = self.load_users()
        self.report = Report()

    def load_orders(self):
        with open(self.order_file, 'r') as file:
            return json.load(file)

    def load_users(self):
        with open(self.users_file, 'r') as file:
            return json.load(file)

    def get_employee_info(self, employee_id):
        for user in self.users:
            if user["id"] == employee_id:
                return {"name": user["name"], "email": user.get("email", "Unknown")}
        return {"name": "Unknown", "email": "Unknown"}

    def show_ordered_items_summary(self):
        date_input = input("Enter date (YYYY, YYYY-MM, or YYYY-MM-DD): ").strip()
        item_counter = Counter()
        order_details = {}

        for order in self.orders:
            order_date = datetime.strptime(order["order_date"], "%d-%b-%Y %I:%M:%p")
            formatted_date = order_date.strftime('%Y-%m-%d')
            formatted_month = order_date.strftime('%Y-%m')
            formatted_year = order_date.strftime('%Y')

            if (len(date_input) == 10 and formatted_date == date_input) or \
               (len(date_input) == 7 and formatted_month == date_input) or \
               (len(date_input) == 4 and formatted_year == date_input):
                
                employee_info = self.get_employee_info(order.get("employee_id", "Unknown"))

                for item in order["order_items"]:
                    item_key = (item["item_id"], item["item_name"])
                    item_counter[item_key] += item["quantity"]

                    if item_key not in order_details:
                        order_details[item_key] = []
                    
                    order_details[item_key].append({
                        "quantity": item["quantity"],
                        "order_date": formatted_date,
                        "order_time": order_date.strftime('%I:%M %p'),
                        "employee_name": employee_info["name"],
                        "employee_email": employee_info["email"]
                    })

        if item_counter:
            self.report.show_order_summary_header(date_input)
            for (item_id, item_name), total_quantity in item_counter.most_common():
                self.report.show_item_summary(item_id, item_name, total_quantity)
                for detail in order_details[(item_id, item_name)]:
                    self.report.show_order_details(detail)
        else:
            self.report.no_orders_found(date_input)
