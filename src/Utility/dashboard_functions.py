# Define color codes
class Colors:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_BLUE = "\033[94m"

def display_main_menu():
    print(f"{Colors.CYAN}{'-'*50}")
    print("============ Owner Dashboard ============")
    print(f"{'-'*50}{Colors.RESET}")
    print(f"\n{Colors.YELLOW}1. Menu Management")
    print("2. Order Management")
    print("3. Invoice Management")
    print("4. Table Booking Management")
    print("5. Staff Management")
    print("6. Reports")
    print("7. Show All Staff")
    print(f"{Colors.RED}{'='*4}7. Logout{'='*4}{Colors.RESET}")

def display_staff_menu():
    print(f"{Colors.CYAN}{'-'*50}")
    print("============ Staff Dashboard ============")
    print(f"{'-'*50}{Colors.RESET}")
    print(f"\n{Colors.YELLOW}1. Order Management")
    print("2. Invoice Management")
    print("3. Table Booking Management")
    print("4. Reports")
    print("5. Display Profile")
    print(f"{Colors.RED}{'='*4}6. Logout{'='*4}{Colors.RESET}")

def display_menu_management():
    print(f"{Colors.BRIGHT_BLUE}{'-'*40}")
    print(f"{'*'*5}🍜 🥂MENU MANAGEMENT🍟 🥘{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.BRIGHT_CYAN}1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Add Stock Ingredient")
    print("5. Check Stock Ingredients")
    print("6. Show Menu")
    print(f"7. EXIT{Colors.RESET}")

def display_order_management():
    print(f"{Colors.BRIGHT_MAGENTA}{'-'*40}")
    print(f"{'*'*5}🌭 🌮 ORDER MANAGEMENT{'*'*5}🍱 🍹")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.CYAN}1. Show Menu")
    print("2. Take New Order")
    print("3. Update Order")
    print("4. Cancel Order")
    print("5. Search Order")
    print("6. See All Orders")
    print(f"7. EXIT{Colors.RESET}")
    

def display_invoice_management():
    print(f"{Colors.BRIGHT_BLUE}{'-'*40}")
    print(f"{'*'*5}💳 💵INVOICE MANAGEMENT🎫 🧾{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.CYAN}1. Generate Bill")
    print("2. Check Bill")
    print("3. Show All Bills")
    print("4. Mark Bill as Paid")
    print("5. Show All Paid Bills")
    print(f"6. EXIT{Colors.RESET}")

def display_table_booking_management():
    print(f"{Colors.CYAN}{'-'*45}")
    print(f"{'*'*5}🪑📅TABLE BOOKING MANAGEMENT 🍽️ 🕒{'*'*5}")
    print(f"{'-'*45}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Reserve a Table")
    print("2. Cancel a Reservation")
    print("3. Update a Reservation")
    print("4. View Table Availability")
    print("5. View Table Reservations")
    print("6. Search Reservation")
    print(f"7. EXIT{Colors.RESET}")

def display_stock_management():
    print(f"{Colors.CYAN}{'-'*40}")
    print(f"{'*'*5}🍅 🥦 📊 Reports 🌽🥕 {'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.BRIGHT_MAGENTA}1. Soon_Stockout_Ingredients")
    print("2. Show Reservation By Date")
    print("3. Show Cancel Reservations")
    print(f"4. Order Report{Colors.RESET}")

def display_staff_management():
    print(f"{Colors.BRIGHT_BLUE}{'-'*40}")
    print(f"{'*'*5}👨‍🍳 🛎️ Staff Management 👩‍🍳 🍽️ {'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.BRIGHT_CYAN}1. Add Employee  ")
    print("2. Display Profile")
    print("3. Update Profile")
    print("4. Delete Employee")
    print("5. Display All Profiles")
    print(f"6. EXIT {Colors.RESET}")
         
