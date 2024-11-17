import json
from datetime import datetime
from Src.Invoice.order import Order
from Src.Invoice.bill import Bill
from Src.Messages.invoice import BillingHandler
from Src.Utility.path_manager import order_file, bill_file
from Src.Utility.validation import *
from Src.Utility.user_input import get_valid_input

class BillingSystem:
    def __init__(self):
        self.orders = self.load_orders()
        self.bills = self.load_bills()
        self.bill_handler = BillingHandler()

    def load_orders(self):
        with open(order_file, "r") as file:
            order_data = json.load(file)
            return [Order(**data) for data in order_data]

    def save_orders(self):
        with open(order_file, "w") as file:
            json.dump([order.to_dict() for order in self.orders], file, indent=4)

    def load_bills(self):
        try:
            with open(bill_file, "r") as file:
                bill_data = json.load(file)
                return bill_data
        except json.JSONDecodeError:
            self.bill_handler.display_warning_invalid_format()
            return []
        except FileNotFoundError:
            self.bill_handler.display_warning_file_not_found()
            return []

    def save_bills(self):
        with open(bill_file, "w") as file:
            json.dump(self.bills, file, indent=4)

    def generate_bill(self):
        order_id = get_valid_input("Enter Order ID to generate bill: ", validate_order_id)
        order = next((order for order in self.orders if order.order_id == order_id), None)
        if not order:
            self.bill_handler.display_order_not_found(order_id)
            return None
        if order.status != "Processing":
            self.bill_handler.display_order_not_in_processing_status(order_id)
            return None
        bill = Bill(order)
        self.bills.append(bill.to_dict())
        order.status = "Billed"
        self.save_orders()
        self.save_bills()
        self.bill_handler.display_bill_generated(order_id, bill.billing_id)
        return bill.to_dict()

    def check_bill(self):
        billing_id = get_valid_input("Enter Billing ID to check bill: ", validate_billing_id)
        bill = next((bill for bill in self.bills if bill["billing_id"] == billing_id), None)
        if not bill:
            self.bill_handler.display_billing_id_not_found(billing_id)
            return None
        self.bill_handler.print_bill(bill)

    def show_all_bills(self):
        if not self.bills:
            self.bill_handler.display_no_bills_found()
            return
        for bill in self.bills:
            self.bill_handler.print_bill(bill)

    def mark_as_paid(self):
        billing_id = get_valid_input("Enter Billing ID to mark as paid: ", validate_billing_id)
        bill = next((bill for bill in self.bills if bill["billing_id"] == billing_id), None)
        if not bill:
            self.bill_handler.display_billing_id_not_found(billing_id)
            return
        if bill["status"] == "Paid":
            self.bill_handler.display_bill_paid_already()
            return
        
        # Display the total amount due for the bill
        self.bill_handler.display_required_payment_amount(bill["total"])


        # Loop to ensure a valid payment type
        while True:
            payment_type = input("Enter Payment Type (Online/Cash): ").capitalize()
            if payment_type in ["Online", "Cash"]:
                break
            else:
                self.bill_handler.display_invalid_payment_type()
        
        # Display the required payment amount
        self.bill_handler.display_required_payment_amount(bill["total"])
        
        # Loop to ensure correct payment amount
        while True:
            try:
                payment_amount = float(input("Enter Payment Amount: ₹"))
                if payment_amount == bill["total"]:
                    break
                else:
                    self.bill_handler.display_invalid_payment_amount()
            except ValueError:
                self.bill_handler.display_invalid_amount_input()

        # Mark the bill as paid
        bill["status"] = "Paid"
        bill["payment_type"] = payment_type
        bill["payment_date"] = datetime.now().strftime("%d-%b-%Y %I:%M %p")

        self.save_bills()
        self.bill_handler.display_payment_success(billing_id)

    def show_all_paid_bills(self):
        paid_bills = [bill for bill in self.bills if bill["status"] == "Paid"]
        if not paid_bills:
            self.bill_handler.display_no_paid_bills_found()
            return
        for bill in paid_bills:
            self.bill_handler.print_bill(bill)
    
    def exit_system(self):
        self.bill_handler.exit_message()
    
    def welcome_system(self):
        self.bill_handler.welcome_message()
