from Src.Utility.color import Colors
color = Colors()

def display_main_menu():
    print(f"{Colors.LIGHT_CORAL}{'-'*50}")
    print("\t============ Owner Dashboard ============")
    print(f"{'-'*50}{Colors.RESET}")
    print(f"\n{Colors.LIGHT_TEAL}1. Menu Management")
    print("2. Order Management")
    print("3. Invoice Management")
    print("4. Table Booking Management")
    print("5. Staff Management")
    print("6. Reports")
    print(f"7. Show All Staff{Colors.RESET}")
    print(f"{Colors.LIGHT_ORANGE}{'='*4}8. Logout{'='*4}{Colors.RESET}")

def display_staff_menu():
    print(f"{Colors.LIGHT_TEAL}{'-'*50}")
    print("\t============ Staff Dashboard ============")
    print(f"{'-'*50}{Colors.RESET}")
    print(f"\n{Colors.LIGHT_ORANGE}1. Order Management")
    print("2. Invoice Management")
    print("3. Table Booking Management")
    print("4. Reports")
    print(f"5. Display Profile{Colors.RESET}")
    print(f"{Colors.LIGHT_PINK}{'='*4}6. Logout{'='*4}{Colors.RESET}")

def display_menu_management():
    print(f"{Colors.LIGHT_VIOLET}{'-'*40}")
    print(f"\t{'*'*5}MENU MANAGEMENT{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.BRIGHT_CYAN}1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Add Stock Ingredient")
    print("5. Check Stock Ingredients")
    print(f"6. Show Menu{Colors.RESET}")
    print(f"{Colors.LIGHT_CORAL}7. EXIT{Colors.RESET}")

def display_order_management():
    print(f"{Colors.LIGHT_PEACH}{'-'*40}")
    print(f"\t{'*'*5} ORDER MANAGEMENT{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.CYAN}1. Show Menu")
    print("2. Take New Order")
    print("3. Update Order")
    print("4. Cancel Order")
    print("5. Search Order")
    print(f"6. See All Orders{Colors.RESET}")
    print(f"{Colors.LIGHT_BLUE}7. EXIT{Colors.RESET}")
    

def display_invoice_management():
    print(f"{Colors.LIGHT_ORANGE}{'-'*40}")
    print(f"\t{'*'*5}INVOICE MANAGEMENT{'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.LIGHT_BLUE}1. Generate Bill")
    print("2. Check Bill")
    print("3. Show All Bills")
    print("4. Mark Bill as Paid")
    print(f"5. Show All Paid Bills{Colors.RESET}")
    print(f"{Colors.LIGHT_PINK}6. EXIT{Colors.RESET}")

def display_table_booking_management():
    print(f"{Colors.CYAN}{'-'*45}")
    print(f"\t{'*'*5}TABLE BOOKING MANAGEMENT {'*'*5}")
    print(f"{'-'*45}{Colors.RESET}")
    print(f"\n{Colors.GREEN}1. Reserve a Table")
    print("2. Cancel a Reservation")
    print("3. Update a Reservation")
    print("4. View Table Availability")
    print("5. View Table Reservations")
    print(f"6. Search Reservation{Colors.RESET}")
    print(f"{Colors.LIGHT_LIME}7. EXIT{Colors.RESET}")

def display_stock_management():
    print(f"{Colors.LIGHT_ORANGE}{'-'*40}")
    print(f"\t{'*'*5} Reports {'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.LIGHT_CORAL}1. Soon_Stockout_Ingredients")
    print("2. Show Reservation By Date")
    print("3. Show Cancel Reservations")
    print(f"4. Order Report{Colors.RESET}")
    print(f"{Colors.LIGHT_TEAL}5. EXIT {Colors.RESET}")

def display_staff_management():
    print(f"{Colors.LIGHT_SKY_BLUE}{'-'*40}")
    print(f"\t{'*'*5} Staff Management  {'*'*5}")
    print(f"{'-'*40}{Colors.RESET}")
    print(f"\n{Colors.LIGHT_GREEN}1. Add Employee  ")
    print("2. Display Profile")
    print("3. Update Profile")
    print("4. Delete Employee")
    print(f"{Colors.LIGHT_PEACH}5. Display All Profiles")
    print(f"{Colors.LIGHT_VIOLET}6. EXIT {Colors.RESET}")
         
