import json
from datetime import datetime, timedelta
from Src.Utility.path_manager import bill_file

class BillReport:
    def __init__(self,bill_file=bill_file):
        # Load billing data from JSON file
        self.bill_file = bill_file
        self.bills = self.load_billing_data()

    def load_billing_data(self):
        try:
            with open(self.bill_file, "r") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError
                return data
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            print("⚠️ Warning: 'billing.json' is empty or has invalid format. Initializing with an empty list.")
            return []

    def generate_report(self):
        date_filter = self.get_date_filter()
        self.display_bill_report(date_filter)

    def get_date_filter(self):
        while True:
            filter_type = input("Select Date Filter: Year, Month, Day, Last Week\nEnter filter (year/month/day/last_week): ").strip().lower()
            if filter_type not in ["year", "month", "day", "last_week"]:
                print("Invalid filter type. Please enter 'year', 'month', 'day', or 'last_week'.")
                continue

            try:
                if filter_type == "day":
                    date_str = input("Enter date (dd-mm-yyyy): ")
                    filter_date = datetime.strptime(date_str, "%Y-%m-%d")
                    return {"type": "day", "value": filter_date}
                elif filter_type == "month":
                    year = int(input("Enter year (e.g., 2024): "))
                    month = int(input("Enter month (1-12): "))
                    filter_date = datetime(year, month, 1)
                    return {"type": "month", "value": filter_date}
                elif filter_type == "year":
                    year = int(input("Enter year (e.g., 2023): "))
                    filter_date = datetime(year, 1, 1)
                    return {"type": "year", "value": filter_date}
                elif filter_type == "last_week":
                    current_date = datetime.now()
                    start_date = current_date - timedelta(days=current_date.weekday() + 7)
                    return {"type": "last_week", "value": start_date}
            except ValueError:
                print("Invalid date. Please try again.")

    def display_bill_report(self, date_filter):
        filtered_bills = self.filter_bills_by_date(date_filter)
        if not filtered_bills:
            print("❌ No bills found.")
        else:
            print("\n--- Bill Report ---")
            for bill in filtered_bills:
                print(f"Billing ID: {bill['billing_id']}")
                print(f"Total: ₹{bill['total']}")
                print(f"Payment Type: {bill['payment_type']}")
                print(f"Payment Date: {bill['payment_date']}")
                print(f"Status: {bill['status']}")
                print("-" * 20)

    def filter_bills_by_date(self, date_filter):
        filtered_bills = []
        for bill in self.bills:
            payment_date_str = bill.get("payment_date")
            
            if not payment_date_str:
                continue  # Skip if payment_date is None or missing

            try:
                # Attempt to parse the payment date
                payment_date = datetime.strptime(payment_date_str, "%d-%b-%Y %I:%M %p")
            except ValueError:
                print(f"⚠️ Warning: Skipping invalid date format in bill with ID {bill.get('billing_id')}")
                continue  # Skip this entry if the format is incorrect

            if date_filter["type"] == "day":
                if payment_date.date() == date_filter["value"].date():
                    filtered_bills.append(bill)
            elif date_filter["type"] == "month":
                if payment_date.year == date_filter["value"].year and payment_date.month == date_filter["value"].month:
                    filtered_bills.append(bill)
            elif date_filter["type"] == "year":
                if payment_date.year == date_filter["value"].year:
                    filtered_bills.append(bill)
            elif date_filter["type"] == "last_week":
                start_date = date_filter["value"]
                end_date = start_date + timedelta(days=7)
                if start_date <= payment_date < end_date:
                    filtered_bills.append(bill)

        return filtered_bills
