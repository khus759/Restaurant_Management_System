class BillingHandler:
    # Define color codes
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BRIGHT_MAGENTA = "\033[95m"

    def display_warning_invalid_format(self):
        print(f"{self.YELLOW}⚠️ Warning: 'billing.json' is empty or has invalid format. Initializing with an empty list.{self.RESET}")
    
    def display_warning_file_not_found(self):
        print(f"{self.YELLOW}⚠️ Warning: 'billing.json' file not found. A new file will be created.{self.RESET}")

    def display_order_not_found(self, order_id):
        print(f"{self.RED}Order with ID {order_id} not found.{self.RESET}")
    
    def display_order_not_in_processing_status(self, order_id):
        print(f"{self.RED}Order ID {order_id} is not in 'Processing' status and cannot be billed.{self.RESET}")

    def display_bill_generated(self, order_id, billing_id):
        print(f"{self.GREEN}✔️ Bill generated successfully for Order ID {order_id}. Billing ID: {billing_id}{self.RESET}")

    def display_billing_id_not_found(self, billing_id):
        print(f"{self.RED}❌ Billing ID {billing_id} not found.{self.RESET}")

    def display_no_bills_found(self):
        print(f"{self.RED}❌ No bills found.{self.RESET}")

    def display_bill_paid_already(self):
        print(f"{self.RED}❌ This bill has already been paid.{self.RESET}")

    def display_invalid_payment_type(self):
        print(f"{self.RED}❌ Invalid payment type. Please enter 'Online' or 'Cash'.{self.RESET}")

    def display_payment_amount_mismatch(self):
        print(f"{self.RED}❌ Payment amount does not match the bill total. Please try again.{self.RESET}")

    def display_payment_success(self, billing_id):
        print(f"{self.GREEN}✔️ Payment successful for Billing ID {billing_id}. Status updated to 'Paid'.{self.RESET}")

    def display_no_paid_bills_found(self):
        print(f"{self.RED}❌ No paid bills found.{self.RESET}")

    def display_all_bills(self, bills):
        if bills:
            print(f"{self.BLUE}All Bills:{self.RESET}")
            for bill in bills:
                self.display_single_bill(bill)
        else:
            print(f"{self.RED}❌ No bills found.{self.RESET}")

    def display_single_bill(self, bill):
        
        print(f"{self.BLUE}Billing ID: {bill['billing_id']}{self.RESET}")
        print(f"Order ID: {bill['order_id']}")
        print(f"Customer Name: {bill['customer_name']}")
        print(f"Billing Date: {bill['billing_date']}")
        print(f"Subtotal: ₹{bill['subtotal']}")
        print(f"GST: ₹{bill['gst']}")
        print(f"Total: ₹{bill['total']}")
        print(f"Status: {bill['status']}")
        print(f"Payment Type: {bill['payment_type']}")
        print(f"Payment Date: {bill['payment_date']}")
        print(f"{self.GREEN}={self.RESET}" * 40)
    
    def print_bill(self, bill):
        print("\n" )
        print(f"{self.BRIGHT_MAGENTA}               BILL DETAILS                {self.RESET}")
        print(f"{self.YELLOW}={self.RESET}" * 50)
        print(f"{self.GREEN}Billing ID: {bill['billing_id']}{self.RESET}")
        print(f"Order ID: {bill['order_id']}")
        print(f"Customer Name: {bill['customer_name']}")
        print(f"Billing Date: {bill['billing_date']}")
        print(f"{self.YELLOW}-{self.RESET}" * 50)
        print("\nItems Purchased:")
        for i, item in enumerate(bill['items'], start=1):
            print(f"  {i}. {item['item_name']} (Size: {item['size']}) x{item['quantity']} = ₹{item['total_price']:.2f}")
        print(f"{self.YELLOW}-{self.YELLOW}" * 50)
        print(f"\nSubtotal: ₹{bill['subtotal']:.2f}")
        print(f"GST (18%): ₹{bill['gst']:.2f}")
        print(f"Total: ₹{bill['total']:.2f}")
        print(f"Status: {bill['status']}")
        if bill["status"] == "Paid":
            print(f"Payment Type: {bill['payment_type']}")
            print(f"Payment Date: {bill['payment_date']}")
        print(f"{self.YELLOW}-{self.RESET}" * 50)
    
    def welcome_message(self):
        print(f"{self.BLUE} 😀 Welcome to the Invoice System! Please follow the prompts to continue.{self.RESET}")

    def exit_message(self):
        print(f"{self.BLUE} 😀 Thank you for using the Invoice System. Goodbye!{self.RESET}")
