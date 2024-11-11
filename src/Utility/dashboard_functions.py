
def display_main_menu():
    print("\n********* Owner Dashboard *********")
    print("1. Menu Management")
    print("2. Order Management")
    print("3. Invoice Management")
    print("4. Table Booking Management")
    print(f"{'-'*4}5. Logout{'-'*4}")

def display_staff_menu():
    print("\n********* Staff Dashboard *********")
    print("1. Order Management")
    print("2. Invoice Management")
    print("3. Table Booking Management")
    print(f"{'-'*4}5. Logout{'-'*4}")


def display_menu_management():
    print(f"\n{'*'*5}MENU MANAGEMENT{'*'*5}")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Add Stock Ingredient")
    print("5. Check Stock Ingredients")
    print("6. Show Menu")

def display_order_management():
    print(f"\n{'*'*5}ORDER MANAGEMENT{'*'*5}")
    print("1. Show Menu")
    print("2. Take New Order")
    print("3. Update Order")
    print("4. Cancel Order")
    print("5. Search Order")
    print("6. See All Orders")
    
def display_invoice_management():
    print(f"\n{'*'*5}INVOICE MANAGEMENT{'*'*5}")
    print("1. Generate Invoice")
    print("2. Search Invoice")
    print("3. Show All Invoices")

def display_table_booking_management():
    print(f"\n{'*'*5}TABLE BOOKING MANAGEMENT{'*'*5}")
    print("1. Reserve a Table")
    print("2. Cancel a Reservation")
    print("3. Update a Reservation")
    print("4. View Table Availability")
    print("5. View Table Reservations")
    print("6. Search Reservation")

