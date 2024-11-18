from Src.Menu_management.menu_feature import MenuManagement
from Src.Booking_Table.table_booking_system import TableBookingSystem
from Src.Utility.ask_dashboard import ask_for_dashboard
from Src.Utility.dashboard_functions import (
    display_main_menu,
    display_menu_management,
    display_order_management,
    display_invoice_management,
    display_table_booking_management,
    display_stock_management,
    display_staff_management   
)
from Src.Order_management.order_features import OrderManagementSystem
from Src.Reports.soon_stock_out import ExpirationReport
from Src.Reports.booking import ReservationReport
from Src.Reports.order_report import OrderReport
from Src.Invoice.bill_system import BillingSystem
from Src.Authentication.auth_system import AuthSystem
from Src.Staff_Management.staff_system import StaffManagementSystem
from Src.Messages.reports import Report
from Src.Reports.bill_report import BillReport
from Src.Staff_Management.salary import SalaryManagement


class OwnerDashboard:
    def __init__(self):
        self.menu_management = MenuManagement()
        self.booking_system = TableBookingSystem()
        self.order_management = OrderManagementSystem()
        self.soon_expire_ingredients = ExpirationReport()
        self.reserve_table = ReservationReport()
        self.order_reports = OrderReport()
        self.bill_system = BillingSystem()
        self.auth = AuthSystem()
        self.staff = StaffManagementSystem()
        self.report = Report()
        self.bill_report = BillReport()
        self.salary = SalaryManagement()
        
    
    def display_dashboard(self):
        while True:
            display_main_menu()
            main_choice = input("Choose a Option: ")

            if main_choice == "1":
                self.handle_menu_management()
            elif main_choice == "2":
                self.handle_order_management()
            elif main_choice == "3":
                self.handle_invoice_management()
            elif main_choice == "4":
                self.handle_table_booking_management()
            elif main_choice == "5":
                self.handle_staff_management()
            elif main_choice == "6":
                self.handle_stock_management()
            elif main_choice == "7":
                self.auth.show_all_staff()
            elif main_choice == "8":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

            if not ask_for_dashboard():
                break

    def handle_menu_management(self):
        self.menu_management.welcome()
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
        elif choice == "7":
            self.menu_management.exit()
        else:
            print("Invalid choice in Menu Management.")
        
    def handle_order_management(self):
        self.order_management.welcome_system()
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
        elif choice == "7":
            self.order_management.exit_system()
        else:
            print("Invalid choice in Order Management.")

    def handle_invoice_management(self):
        self.bill_system.welcome_system()
        display_invoice_management()
        
        choice = input("Choose an action in Invoice system : ")
        if choice == "1":
            self.bill_system.generate_bill()
        elif choice == "2":
            self.bill_system.check_bill()
        elif choice == "3":
            self.bill_system.show_all_bills()
        elif choice == "4":
            self.bill_system.mark_as_paid()
        elif choice == "5":
            self.bill_system.show_all_paid_bills()
        elif choice == "6": 
            self.bill_system.exit_system() 
        else: 
            print("Invalid choice in Invoice Management.")


    def handle_table_booking_management(self):
        self.booking_system.welcome_system()
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
        elif choice == "7":
            self.booking_system.exit_system()
        else:
            print("Invalid choice in Table Booking Management.")
    
    def handle_stock_management(self):
        self.report.welcome_message()
        display_stock_management()

        choice = input("Choose an action in Reports Management: ")

        if choice == "1":
            self.soon_expire_ingredients.display_report()
        elif choice == "2":
            self.reserve_table.show_reservations_by_date()
        elif choice == "3":
            self.reserve_table.show_canceled_reservations()
        elif choice == "4":
            self.order_reports.show_ordered_items_summary()
        elif choice == "5":
            self.bill_report.generate_report()
        elif choice == "6":
            self.report.exit_message()
        else:
            print("Invalid choice in Reports Management.")
    
    def handle_staff_management(self):
        self.staff.welcome_system()
        display_staff_management()

        choice = input("Choose an action in Staff Management: ")

        if choice == "1":
            self.staff.add_employee()
        elif choice == "2":
            self.staff.display_profile()
        elif choice == "3":
            self.staff.update_profile()
        elif choice == "4":
            self.staff.delete_employee()
        elif choice == "5":
            self.staff.display_all_profiles()
        elif choice == "6":
            self.salary.pay_salary()
        elif choice == "7":
            self.salary.show_salary_history()
        elif choice == "8":
            self.staff.exit_system()
        else:
            print("Invalid choice in Staff Management.")
    