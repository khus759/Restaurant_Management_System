import json
from datetime import datetime
from collections import defaultdict
from Src.Utility.path_manager import bill_file
from Src.Messages.invoice import BillingHandler


class BillReport:
    def __init__(self, bill_file=bill_file):
        self.bill_file = bill_file
        self.bill_handler = BillingHandler()
        self.bills = self.load_bills()

    def load_bills(self):
        """Load bills from the JSON file."""
        try:
            with open(self.bill_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.bill_handler.display_warning_invalid_format()
            return []

    def get_date_input(self, prompt):
        """
        Prompt the user to enter a date and validate the format.
        :param prompt: Prompt message for the input.
        :return: Parsed datetime object or None if invalid.
        """
        date_format = "%d-%b-%Y %I:%M %p"
        while True:
            date_input = input(prompt)
            try:
                return datetime.strptime(date_input, date_format)
            except ValueError:
                self.bill_handler.display_invalid_date_format()

    def generate_report(self):
        """
        Generate a report of bills within the date range.
        If no date range is provided, all bills are included.
        """
        self.bill_handler.display_report_start()
        start_date = self.get_date_input("Enter start date (DD-MMM-YYYY HH:MM AM/PM): ")
        end_date = self.get_date_input("Enter end date (DD-MMM-YYYY HH:MM AM/PM): ")

        report = []
        date_format = "%d-%b-%Y %I:%M %p"

        for bill in self.bills:
            try:
                bill_date = datetime.strptime(bill["billing_date"], date_format)
                if start_date and bill_date < start_date:
                    continue
                if end_date and bill_date > end_date:
                    continue
                report.append(bill)
            except ValueError:
                self.bill_handler.display_invalid_date_format()
                continue

        if not report:
            self.bill_handler.display_no_bills_found_in_report()
            return []

        self.bill_handler.display_report_success(len(report))
        return report

    def total_sales(self):
        """Calculate total sales."""
        total = sum(bill["total"] for bill in self.bills if bill["status"] == "Paid")
        self.bill_handler.display_total_sales(total)
        return total

    def sales_by_payment_type(self):
        """Generate sales breakdown by payment type."""
        breakdown = defaultdict(float)
        for bill in self.bills:
            if bill["status"] == "Paid" and bill["payment_type"]:
                breakdown[bill["payment_type"]] += bill["total"]
        self.bill_handler.display_sales_by_payment_type(breakdown)
        return breakdown

    def sales_summary(self):
        """Generate a summary report of total sales and payment breakdown."""
        self.bill_handler.display_sales_summary_start()
        total_sales = self.total_sales()
        breakdown = self.sales_by_payment_type()
        summary = {
            "total_sales": total_sales,
            "breakdown_by_payment": breakdown
        }
        self.bill_handler.display_sales_summary(summary)
        return summary
