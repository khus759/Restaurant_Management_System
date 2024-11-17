import json
from datetime import datetime
from collections import Counter
from Src.Utility.path_manager import order_file, users_file

class OrderReport:
    def __init__(self, order_file=order_file, users_file=users_file):
        self.order_file = order_file
        self.users_file = users_file
        self.orders = self.load_orders()
        self.users = self.load_users()

    def load_orders(self):
        with open(self.order_file, 'r') as file:
            return json.load(file)

    def load_users(self):
        with open(self.users_file, 'r') as file:
            return json.load(file)

    def get_employee_name(self, employee_id):
        # Fetch employee name based on ID
        for user in self.users:
            if user["id"] == employee_id:
                return user["name"]
        return "Unknown"

    def show_ordered_items_summary(self):
        # Taking user input for date filter (year, month, or day)
        date_input = input("Enter date (YYYY, YYYY-MM, or YYYY-MM-DD): ").strip()

        # Define counters for item frequencies and to store additional order info
        item_counter = Counter()
        order_details = {}

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
                
                # Check if 'employee_id' exists in the order
                employee_id = order.get("employee_id", "Unknown")
                employee_name = self.get_employee_name(employee_id) if employee_id != "Unknown" else "Unknown"

                for item in order["order_items"]:
                    item_key = (item["item_id"], item["item_name"])
                    item_counter[item_key] += item["quantity"]
                    
                    # Store details by item with order date, time, and employee info
                    if item_key not in order_details:
                        order_details[item_key] = []
                    
                    order_details[item_key].append({
                        "quantity": item["quantity"],
                        "order_date": formatted_date,
                        "order_time": order_date.strftime('%I:%M %p'),
                        "employee_name": employee_name
                    })

        # Display ordered items summary with details
        if item_counter:
            print(f"\nItem Order Summary for {date_input}:")
            for (item_id, item_name), total_quantity in item_counter.most_common():
                print(f"\nItem ID: {item_id}, Item Name: {item_name}, Total Quantity Ordered: {total_quantity}")
                for detail in order_details[(item_id, item_name)]:
                    print(f"  - Quantity: {detail['quantity']}, Date: {detail['order_date']}, Time: {detail['order_time']}, Taken by: {detail['employee_name']}")
        else:
            print(f"No orders found for the specified date: {date_input}")

# Usage
# if __name__ == "__main__":
#     report = OrderReport()
#     report.show_ordered_items_summary()
