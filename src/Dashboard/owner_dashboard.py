from Src.Menu_management.menu_feature import MenuManagement
from Src.Booking_Table.table_booking_system import TableBookingSystem
from Src.Utility.ask_dashboard import ask_for_dashboard
from Src.Utility.dashboard_functions import (
    display_main_menu,
    display_menu_management,
    display_order_management,
    display_invoice_management,
    display_table_booking_management   
)
from Src.Order_management.order_features import OrderManagementSystem


class OwnerDashboard:
    def __init__(self):
        self.menu_management = MenuManagement()
        self.booking_system = TableBookingSystem()
        self.order_management = OrderManagementSystem()
    
    def display_dashboard(self):
        while True:
            display_main_menu()
            main_choice = input("Choose a category: ")

            if main_choice == "1":
                self.handle_menu_management()
            elif main_choice == "2":
                self.handle_order_management()
            elif main_choice == "3":
                self.handle_invoice_management()
            elif main_choice == "4":
                self.handle_table_booking_management()
            elif main_choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

            if not ask_for_dashboard():
                break

    def handle_menu_management(self):
        display_menu_management()
        choice = input("Choose an action in Menu Management: ")

        if choice == "1":
            self.menu_management.add_item()
        elif choice == "2":
            self.menu_management.update_item()
        elif choice == "3":
            self.menu_management.delete_item()
        elif choice == "4":
            self.menu_management.add_stock_ingredient()
        elif choice == "5":
            self.menu_management.check_stock_ingredients()
        elif choice == "6":
            self.menu_management.show_menu()
        else:
            print("Invalid choice in Menu Management.")
        
    def handle_order_management(self):
        display_order_management()
        choice = input("Choose an action in Order Management: ")

        if choice == "1":
            self.order_management.show_menu()
        elif choice == "2":
            self.order_management.take_order()
        elif choice == "3":
            self.order_management.update_order()
        elif choice == "4":
            self.order_management.cancel_order()
        elif choice == "5":
            self.order_management.check_order()
        elif choice == "6":
            self.order_management.show_all_orders()
        else:
            print("Invalid choice in Order Management.")

    def handle_invoice_management(self):
        display_invoice_management()
        print("Invoice Management features are under development.")

    def handle_table_booking_management(self):
        display_table_booking_management()
        choice = input("Choose an action in Table Booking Management: ")

        if choice == "1":
            self.booking_system.reserve_table()
        elif choice == "2":
            self.booking_system.cancel_reservation()
        elif choice == "3":
            self.booking_system.update_reservation()
        elif choice == "4":
            self.booking_system.view_availability()
        elif choice == "5":
            self.booking_system.view_all_reservations()
        elif choice == "6":
            self.booking_system.search_reservation_by_id()
        else:
            print("Invalid choice in Table Booking Management.")
