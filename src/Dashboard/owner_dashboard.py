
from Src.Menu_management.menu_feature import MenuManagement
from Src.Booking_Table.table_booking_system import TableBookingSystem

from Src.Utility.ask_dashboard import ask_for_dashboard

class OwnerDashboard:
    def __init__(self):
        self.menu_management = MenuManagement()
        self.booking_system = TableBookingSystem()

        
    def display_dashboard(self):
        while True:
            print("\n********* Owner Dashboard *********")
            print(f"{'-'*5}MENU{'-'*5}")
            print("1. Show Menu")
            print("2. Add Menu Item")
            print("3. Update Menu Item")
            print("4. Delete Menu Item")
            print(f"\n{'-'*5}ORDER{'-'*5}")
            print("5. Take New Order")
            print("6. Update Order")
            print("7. Cancel Order")
            print("8. See All Order ")
            print("9. Find Order")
            print(f"\n{'-'*5}INVOICE{'-'*5}")
            print("10. Invoice")
            print("11. Search Invoice")
            print("12. Show Invoice")
            print(f"\n{'-'*5}TABLE BOOKING{'-'*5}")
            print("13. Reserve a table")
            print("14. Cancel a reservation")
            print("15. Update a reservation")
            print("16. View table availability")
            print("17. Logout")

            try:
                action = input("Choose an action: ")
            except:
                print("please choose valid input")
                continue

            if action == "1":
                self.menu_management.show_menu()
            elif action == "2":
                self.menu_management.add_menu_item()
            elif action == "3":
                self.menu_management.update_menu_item()
            elif action == "4":
                self.menu_management.delete_menu_item()
            elif action == "13":
                self.booking_system.reserve_table()
            elif action == "14":
                self.booking_system.cancel_reservation()
            elif action == "15":
                self.booking_system.update_reservation()
            elif action == "16":
                self.booking_system.view_availability()
            elif action == "17":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")
            
            if not ask_for_dashboard():
                break



# def run():
#     system = OrderManagementSystem()
#     while True:
#         print("\nOrder Management System")
#         print("1. Take New Order")
#         print("2. Update Order")
#         print("3. Cancel Order")
#         print("4. Display Menu")
#         print("5. See All Orders")
#         print("6. Find Order")
#         print("7. Exit")

#         choice = input("Enter your choice: ")
#         if choice == '1':
#             system.take_order()
#         elif choice == '2':
#             system.update_order()
#         elif choice == '3':
#             system.cancel_order()
#         elif choice == '4':
#             system.menu.display()
#         elif choice == '5':
#             system.see_all_orders()
#         elif choice == '6':
#             system.find_order()
#         elif choice == '7':
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     run()
