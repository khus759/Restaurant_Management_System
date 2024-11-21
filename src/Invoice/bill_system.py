import json
from datetime import datetime
from Src.Invoice.order import Order
from Src.Invoice.bill import Bill
from Src.Messages.invoice import BillingHandler
from Src.Utility.path_manager import order_file, bill_file
from Src.Utility.validation import *
from Src.Utility.user_input import get_valid_input


class BillingSystem:
    def __init__(self, order_file=order_file, bill_file=bill_file):
        self.order_file = order_file
        self.bill_file = bill_file
        self.orders = self.load_orders()
        self.bills = self.load_bills()
        self.bill_handler = BillingHandler()

    def load_orders(self):
        """Load orders from JSON file."""
        try:
            with open(self.order_file, "r") as file:
                order_data = json.load(file)
                return [Order(**data) for data in order_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.bill_handler.display_warning_invalid_format()
            return []

    def save_orders(self):
        """Save orders to JSON file and synchronize data."""
        try:
            with open(self.order_file, "w") as file:
                json.dump([order.to_dict() for order in self.orders], file, indent=4)
                self.bill_handler.display_save_success("Orders")
        except Exception as e:
            self.bill_handler.display_save_error("Orders")

    def reload_orders(self):
        """Reload orders to synchronize in-memory data with the file."""
        self.orders = self.load_orders()

    def load_bills(self):
        """Load bills from JSON file."""
        try:
            with open(self.bill_file, "r") as file:
                bill_data = json.load(file)
                return bill_data
        except (FileNotFoundError, json.JSONDecodeError):
            self.bill_handler.display_warning_invalid_format()
            return []

    def save_bills(self):
        """Save bills to JSON file."""
        try:
            with open(self.bill_file, "w") as file:
                json.dump(self.bills, file, indent=4)
                self.bill_handler.display_save_success("Bills")
        except Exception as e:
            self.bill_handler.display_save_error("Bills")

    def reload_bills(self):
        """Reload bills to synchronize in-memory data with the file."""
        self.bills = self.load_bills()

    def place_order(self, item_id, quantity):
        """Place a new order and save it to the order list and file."""
        new_order = Order(item_id=item_id, quantity=quantity, status="Processing")
        self.orders.append(new_order)  # Add the new order to the in-memory list
        self.save_orders()  # Save orders to file
        self.reload_orders()  # Synchronize in-memory orders with file
        return new_order

    def generate_bill(self):
        """Generate a new bill for a selected order."""
        self.reload_orders()  # Synchronize orders with the file
        self.bill_handler.display_bill_generation_start()
        available_orders = [order.order_id for order in self.orders if order.status == "Processing"]
        self.bill_handler.display_available_orders(available_orders)
        if not available_orders:
            self.bill_handler.display_no_orders_for_billing()
            return

        order_id = get_valid_input("Enter Order ID to generate bill: ", validate_order_id)
        self.bill_handler.display_order_id(order_id)

        order = next((order for order in self.orders if order.order_id == order_id), None)
        if not order:
            self.bill_handler.display_order_not_found(order_id)
            return None

        if order.status != "Processing":
            self.bill_handler.display_order_not_in_processing_status(order_id)
            return None

        bill = Bill(order)
        self.bills.append(bill.to_dict())
        self.bill_handler.display_bill_generated(order_id, bill.billing_id)

        order.status = "Billed"
        self.save_orders()  # Save orders to update status
        self.save_bills()  # Save the new bill
        return bill.to_dict()

    def check_bill(self):
        """Check details of a specific bill."""
        self.bill_handler.display_bill_check_start()
        billing_id = get_valid_input("Enter Billing ID to check bill: ", validate_billing_id)
        self.bill_handler.display_billing_id(billing_id)
        bill = next((bill for bill in self.bills if bill["billing_id"] == billing_id), None)
        if not bill:
            self.bill_handler.display_billing_id_not_found(billing_id)
            return None
        self.bill_handler.print_bill(bill)

    def show_all_bills(self):
        """Display all bills."""
        self.bill_handler.display_all_bills_start()
        if not self.bills:
            self.bill_handler.display_no_bills_found()
            return
        for bill in self.bills:
            self.bill_handler.print_bill(bill)
        self.bill_handler.display_all_bills(self.bills)

    def mark_as_paid(self):
        """Mark a bill as paid."""
        self.bill_handler.display_bill_marking_start()
        available_bills = [(bill["billing_id"], bill["total"]) for bill in self.bills if bill["status"] != "Paid"]
        self.bill_handler.display_available_bills(available_bills)
        if not available_bills:
            self.bill_handler.display_no_bills_for_payment()
            return

        billing_id = get_valid_input("Enter Billing ID to mark as paid: ", validate_billing_id)
        self.bill_handler.display_billing_id(billing_id)
        bill = next((bill for bill in self.bills if bill["billing_id"] == billing_id), None)
        if not bill:
            self.bill_handler.display_billing_id_not_found(billing_id)
            return

        if bill["status"] == "Paid":
            self.bill_handler.display_bill_paid_already()
            return

        self.bill_handler.display_required_payment_amount(bill["total"])

        while True:
            payment_type = input("Enter Payment Type (Online/Cash): ").capitalize()
            if payment_type in ["Online", "Cash"]:
                break
            else:
                self.bill_handler.display_invalid_payment_type()

        while True:
            try:
                payment_amount = float(input("Enter Payment Amount: ₹"))
                if payment_amount == bill["total"]:
                    break
                else:
                    self.bill_handler.display_invalid_payment_amount()
            except ValueError:
                self.bill_handler.display_invalid_amount_input()

        bill["status"] = "Paid"
        bill["payment_type"] = payment_type
        bill["payment_date"] = datetime.now().strftime("%d-%b-%Y %I:%M %p")
        self.save_bills()
        self.bill_handler.display_payment_success(billing_id)

    def show_all_paid_bills(self):
        """Display all paid bills."""
        self.bill_handler.display_paid_bills_start()
        paid_bills = [bill for bill in self.bills if bill["status"] == "Paid"]
        if not paid_bills:
            self.bill_handler.display_no_paid_bills_found()
            return
        for bill in paid_bills:
            self.bill_handler.print_bill(bill)
        self.bill_handler.display_all_bills(paid_bills)

    def exit_system(self):
        """Exit the billing system."""
        self.bill_handler.exit_message()

    def welcome_system(self):
        """Display a welcome message."""
        self.bill_handler.welcome_message()
