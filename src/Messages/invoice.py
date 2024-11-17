from Src.Utility.color import Colors
class BillingHandler:
    def __init__(self):
        self.color = Colors()
    

    def display_warning_invalid_format(self):
        print(f"{Colors.YELLOW}⚠️ Warning: 'billing.json' is empty or has invalid format. Initializing with an empty list.{Colors.RESET}")
    
    def display_warning_file_not_found(self):
        print(f"{Colors.YELLOW}⚠️ Warning: 'billing.json' file not found. A new file will be created.{Colors.RESET}")

    def display_order_not_found(self, order_id):
        print(f"{Colors.RED}Order with ID {order_id} not found.{Colors.RESET}")
    
    def display_order_not_in_processing_status(self, order_id):
        print(f"{Colors.RED}Order ID {order_id} is not in 'Processing' status and cannot be billed.{Colors.RESET}")

    def display_bill_generated(self, order_id, billing_id):
        print(f"{Colors.GREEN}✔️ Bill generated successfully for Order ID {order_id}. Billing ID: {billing_id}{Colors.RESET}")

    def display_billing_id_not_found(self, billing_id):
        print(f"{Colors.RED}❌ Billing ID {billing_id} not found.{Colors.RESET}")

    def display_no_bills_found(self):
        print(f"{Colors.RED}❌ No bills found.{Colors.RESET}")

    def display_bill_paid_already(self):
        print(f"{Colors.RED}❌ This bill has already been paid.{Colors.RESET}")

    def display_invalid_payment_type(self):
        print(f"{Colors.RED}❌ Invalid payment type. Please enter 'Online' or 'Cash'.{Colors.RESET}")

    def display_payment_amount_mismatch(self):
        print(f"{Colors.RED}❌ Payment amount does not match the bill total. Please try again.{Colors.RESET}")

    def display_payment_success(self, billing_id):
        print(f"{Colors.GREEN}✔️ Payment successful for Billing ID {billing_id}. Status updated to 'Paid'.{Colors.RESET}")

    def display_no_paid_bills_found(self):
        print(f"{Colors.RED}❌ No paid bills found.{Colors.RESET}")

    def display_all_bills(self, bills):
        if bills:
            print(f"{Colors.BLUE}All Bills:{Colors.RESET}")
            for bill in bills:
                self.display_single_bill(bill)
        else:
            print(f"{Colors.RED}❌ No bills found.{Colors.RESET}")

    def display_single_bill(self, bill):
        
        print(f"{Colors.BLUE}Billing ID: {bill['billing_id']}{Colors.RESET}")
        print(f"Order ID: {bill['order_id']}")
        print(f"Customer Name: {bill['customer_name']}")
        print(f"Billing Date: {bill['billing_date']}")
        print(f"Subtotal: ₹{bill['subtotal']}")
        print(f"GST: ₹{bill['gst']}")
        print(f"Total: ₹{bill['total']}")
        print(f"Status: {bill['status']}")
        print(f"Payment Type: {bill['payment_type']}")
        print(f"Payment Date: {bill['payment_date']}")
        print(f"{Colors.GREEN}={Colors.RESET}" * 40)
    
    def print_bill(self, bill):
        print("\n" )
        print(f"{Colors.BRIGHT_MAGENTA}               BILL DETAILS                {Colors.RESET}")
        print(f"{Colors.YELLOW}={Colors.RESET}" * 50)
        print(f"{Colors.GREEN}Billing ID: {bill['billing_id']}{Colors.RESET}")
        print(f"Order ID: {bill['order_id']}")
        print(f"Customer Name: {bill['customer_name']}")
        print(f"Billing Date: {bill['billing_date']}")
        print(f"{Colors.YELLOW}-{Colors.RESET}" * 50)
        print("\nItems Purchased:")
        for i, item in enumerate(bill['items'], start=1):
            print(f"  {i}. {item['item_name']} (Size: {item['size']}) x{item['quantity']} = ₹{item['total_price']:.2f}")
        print(f"{Colors.YELLOW}-{Colors.YELLOW}" * 50)
        print(f"\nSubtotal: ₹{bill['subtotal']:.2f}")
        print(f"GST (18%): ₹{bill['gst']:.2f}")
        print(f"Total: ₹{bill['total']:.2f}")
        print(f"Status: {bill['status']}")
        if bill["status"] == "Paid":
            print(f"Payment Type: {bill['payment_type']}")
            print(f"Payment Date: {bill['payment_date']}")
        print(f"{Colors.YELLOW}-{Colors.RESET}" * 50)
    
    def welcome_message(self):
        print(f"{Colors.LIGHT_CORAL} 😀 Welcome to the Invoice System! Please follow the prompts to continue.{Colors.RESET}")

    def exit_message(self):
        print(f"{Colors.LIGHT_LIME} 😀 Thank you for using the Invoice System. Goodbye!{Colors.RESET}")
    
    def display_required_payment_amount(self, total):
        print(f"Payment Amount Required: ₹{total:.2f}")
    
    def display_total_amount(self, billing_id, total):
        print(f"Total Amount for Billing ID {billing_id}: ₹{total:.2f} Only")

    def display_invalid_payment_amount(self):
        print("❌ Payment amount mismatch. Please enter the exact amount.")

    def display_invalid_amount_input(self):
        print("❌ Invalid amount. Please enter a numeric value.")

    def prompt_payment_type(self):
        return input("Enter Payment Type (Online/Cash): ").capitalize()

