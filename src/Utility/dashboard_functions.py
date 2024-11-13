# Define color codes
class Colors:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

def display_main_menu():
    print(f"{Colors.CYAN}{'-'*50}")
    print("============ Owner Dashboard ============")
    print(f"{'-'*50}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Menu Management")
    print("2. Order Management")
    print("3. Invoice Management")
    print("4. Table Booking Management")
    print("5. Reports")
    print("6. Show All Staff")
    print(f"{Colors.RED}{'-'*4}7. Logout{'-'*4}{Colors.RESET}")

def display_staff_menu():
    print(f"{Colors.CYAN}{'-'*50}")
    print("============ Staff Dashboard ============")
    print(f"{'-'*50}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Order Management")
    print("2. Invoice Management")
    print("3. Table Booking Management")
    print("4. Reports")
    print(f"{Colors.RED}{'-'*4}5. Logout{'-'*4}{Colors.RESET}")

def display_menu_management():
    print(f"{Colors.CYAN}{'-'*40}")
    print(f"\t{'*'*5}MENU MANAGEMENT{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Add Stock Ingredient")
    print("5. Check Stock Ingredients")
    print("6. Show Menu{Colors.RESET}")

def display_order_management():
    print(f"{Colors.CYAN}{'-'*40}")
    print(f"\t{'*'*5}ORDER MANAGEMENT{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Show Menu")
    print("2. Take New Order")
    print("3. Update Order")
    print("4. Cancel Order")
    print("5. Search Order")
    print("6. See All Orders{Colors.RESET}")

def display_invoice_management():
    print(f"{Colors.CYAN}{'-'*40}")
    print(f"\t{'*'*5}INVOICE MANAGEMENT{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Generate Bill")
    print("2. Check Bill")
    print("3. Show All Bills")
    print("4. Mark Bill as Paid")
    print("5. Show All Paid Bills{Colors.RESET}")

def display_table_booking_management():
    print(f"{Colors.CYAN}{'-'*40}")
    print(f"{'*'*5}TABLE BOOKING MANAGEMENT{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Reserve a Table")
    print("2. Cancel a Reservation")
    print("3. Update a Reservation")
    print("4. View Table Availability")
    print("5. View Table Reservations")
    print("6. Search Reservation{Colors.RESET}")

def display_stock_management():
    print(f"{Colors.CYAN}{'-'*40}")
    print(f"\t{'*'*5} Reports {'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Soon_Stockout_Ingredients")
    print("2. Show Reservation By Date")
    print("3. Show Cancel Reservations")
    print("4. Order Report{Colors.RESET}")
