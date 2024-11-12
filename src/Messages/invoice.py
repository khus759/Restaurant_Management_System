
class BillingHandler():
    def display_warning_invalid_format(self):
        print("⚠️ Warning: 'billing.json' is empty or has invalid format. Initializing with an empty list.")
    
    def display_warning_file_not_found(self):
        print("⚠️ Warning: 'billing.json' file not found. A new file will be created.")

    def display_order_not_found(self, order_id):
        print(f"Order with ID {order_id} not found.")
    
    def display_order_not_in_processing_status(self, order_id):
        print(f"Order ID {order_id} is not in 'Processing' status and cannot be billed.")

    def display_bill_generated(self, order_id, billing_id):
        print(f"✔️ Bill generated successfully for Order ID {order_id}. Billing ID: {billing_id}")

    def display_billing_id_not_found(self, billing_id):
        print(f"❌ Billing ID {billing_id} not found.")

    def display_no_bills_found(self):
        print("❌ No bills found.")

    def display_bill_paid_already(self):
        print("❌ This bill has already been paid.")

    def display_invalid_payment_type(self):
        print("❌ Invalid payment type. Please enter 'Online' or 'Cash'.")

    def display_payment_amount_mismatch(self):
        print("❌ Payment amount does not match the bill total. Please try again.")

    def display_payment_success(self, billing_id):
        print(f"✔️ Payment successful for Billing ID {billing_id}. Status updated to 'Paid'.")

    def display_no_paid_bills_found(self):
        print("❌ No paid bills found.")

    def display_all_bills(self, bills):
        if bills:
            print("All Bills:")
            for bill in bills:
                self.display_single_bill(bill)
        else:
            print("❌ No bills found.")

    def display_single_bill(self, bill):
        print(f"Billing ID: {bill['billing_id']}")
        print(f"Order ID: {bill['order_id']}")
        print(f"Customer Name: {bill['customer_name']}")
        print(f"Billing Date: {bill['billing_date']}")
        print(f"Subtotal: ₹{bill['subtotal']}")
        print(f"GST: ₹{bill['gst']}")
        print(f"Total: ₹{bill['total']}")
        print(f"Status: {bill['status']}")
        print(f"Payment Type: {bill['payment_type']}")
        print(f"Payment Date: {bill['payment_date']}")
        print("=" * 40)
    
    def print_bill(self,bill):
        print("\n" + "-"*40)
        print(f"                BILL DETAILS                ")
        print("-"*40)
        print(f" Billing ID: {bill['billing_id']}")
        print(f" Order ID: {bill['order_id']}")
        print(f" Customer Name: {bill['customer_name']}")
        print(f" Billing Date: {bill['billing_date']}")
        print("-"*40)
        print("\nItems Purchased:")
        for i, item in enumerate(bill['items'], start=1):
            print(f"  {i}. {item['item_name']} (Size: {item['size']}) x{item['quantity']} = ₹{item['total_price']:.2f}")
        print("-"*40)
        print(f"\nSubtotal: ₹{bill['subtotal']:.2f}")
        print(f"GST (18%): ₹{bill['gst']:.2f}")
        print(f"Total: ₹{bill['total']:.2f}")
        print(f"Status: {bill['status']}")
        if bill["status"] == "Paid":
            print(f"Payment Type: {bill['payment_type']}")
            print(f"Payment Date: {bill['payment_date']}")
        print("-"*40)
