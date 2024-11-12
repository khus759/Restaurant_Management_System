
def display_main_menu():
    print("-"*50)
    print("============ Owner Dashboard ============")
    print("-"*50)
    print("\n1. Menu Management")
    print("2. Order Management")
    print("3. Invoice Management")
    print("4. Table Booking Management")
    print("5. Reports")
    print(f"{'-'*4}6. Logout{'-'*4}")

def display_staff_menu():
    print("-"*50)
    print("============ Staff Dashboard ============")
    print("-"*50)
    print("\n1. Order Management")
    print("2. Invoice Management")
    print("3. Table Booking Management")
    print("4. Reports")
    print(f"{'-'*4}5. Logout{'-'*4}")


def display_menu_management():
    print("-"*40)
    print(f"\t{'*'*5}MENU MANAGEMENT{'*'*5}")
    print("-"*40)
    print("\n1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Add Stock Ingredient")
    print("5. Check Stock Ingredients")
    print("6. Show Menu")

def display_order_management():
    print("-"*40)
    print(f"\t{'*'*5}ORDER MANAGEMENT{'*'*5}")
    print("-"*40)
    print("\n1. Show Menu")
    print("2. Take New Order")
    print("3. Update Order")
    print("4. Cancel Order")
    print("5. Search Order")
    print("6. See All Orders")
    
def display_invoice_management():
    print("-"*40)
    print(f"\t{'*'*5}INVOICE MANAGEMENT{'*'*5}")
    print("-"*40)
    print("1. Generate Bill")
    print("2. Check Bill")
    print("3. Show All Bills")
    print("4. Mark Bill as Paid")
    print("5. Show All Paid Bills")
        

def display_table_booking_management():
    print("-"*40)
    print(f"{'*'*5}TABLE BOOKING MANAGEMENT{'*'*5}")
    print("-"*40)
    print("\n1. Reserve a Table")
    print("2. Cancel a Reservation")
    print("3. Update a Reservation")
    print("4. View Table Availability")
    print("5. View Table Reservations")
    print("6. Search Reservation")

def display_stock_management():
    print("-"*40)
    print(f"\t{'*'*5} Reports {'*'*5}")
    print("-"*40)
    print("\n1. Soon_Stockout_Ingredients")
    print("2. Show Reservation By Date")
    print("3. Show Cancel Resevations")
    print("4. Order Report")